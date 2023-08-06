import json
from .backend import API
from .output import Output
from .sort import Sort
from .result import Result
from .software import Software
from .meta import Meta

__version__ = Meta.__version__


class Services:
    """Create a instance to call services"""

    def __init__(self) -> None:
        self.res = Result()
        self.api = API()
        self.software = Software()
        self.columns = []
        self.rows = []
        self.res.raw = {}

    def search(self, pid) -> Result:
        """Service for Search"""
        payload = {"suggestionText": pid}
        self.res.json = self.api.request(
            path="/networkdevice/autosuggest",
            method="POST",
            payload=json.dumps(payload),
        )

        self.columns = ["PID", "Transceiver", "Network Device"]
        self.rows = []

        for pid_type, pids in self.res.json.items():
            if "networkDeviceProductID" in pid_type:
                for pid in pids:
                    self.rows.append([pid["name"], "No", "Yes"])
            if "transceiverProductID" in pid_type:
                for pid in pids:
                    self.rows.append([pid["name"], "Yes", "No"])

        self.res.cli = Output.table(
            title="Cisco TMG Search", columns=self.columns, rows=self.rows
        )
        return self.res

    def lookup(self, pid, network_device=False, product_family=None) -> Result:
        """Lookup specific PID"""
        self.pid = pid
        self.title = f"Cisco TMG Lookup\n{self.pid}"
        """ Get PID IDs from Cisco TMG API"""

        if product_family is not None:
            self.product_family = product_family.split(",")
        else:
            self.product_family = None

        pid = self.search(pid=pid)

        if len(pid.json) == 0:
            self.res.cli = Output.table(
                title="Cisco TMG Lookup\nNo unique PID found",
                columns=self.columns,
                rows=self.rows,
            )
            return self.res

        payload = {
            "cableType": [],
            "dataRate": [],
            "formFactor": [],
            "reach": [],
            "searchInput": [""],
            "osType": [],
            "transceiverProductFamily": [],
            "transceiverProductID": [],
            "networkDeviceProductFamily": [],
            "networkDeviceProductID": [],
        }

        if network_device:
            if "networkDeviceProductID" not in pid.json:
                self.res.raw["rows"] = self.rows
                self.res.cli = Output.table(
                    title="Cisco TMG Lookup\nNo network device PID found",
                    columns=self.columns,
                    rows=self.rows,
                )

                return self.res
            """Check if unique Network PID match against lookup PID"""
            pid.json["networkDeviceProductID"] = [
                network_pid
                for network_pid in pid.json["networkDeviceProductID"]
                if network_pid["name"] == self.pid
            ]
            if len(pid.json["networkDeviceProductID"]) != 1:
                self.res.raw["rows"] = self.rows
                self.res.cli = Output.table(
                    title="Cisco TMG Lookup\nNo unique PID found",
                    columns=self.columns,
                    rows=self.rows,
                )
                return self.res
        else:
            """Check if unique SFP PID match against lookup PID"""
            try:
                pid.json["transceiverProductID"] = [
                    transceiver
                    for transceiver in pid.json["transceiverProductID"]
                    if transceiver["name"] == self.pid
                ]
            except KeyError:
                self.res.raw["rows"] = self.rows
                self.res.cli = Output.table(
                    title="Cisco TMG Lookup\nNo Transceiver PID found",
                    columns=self.columns,
                    rows=self.rows,
                )
                return self.res
            if len(pid.json["transceiverProductID"]) != 1:
                self.res.raw["rows"] = self.rows
                self.res.cli = Output.table(
                    title="Cisco TMG Lookup\nNo unique PID found",
                    columns=self.columns,
                    rows=self.rows,
                )

                return self.res

        payload = payload | pid.json

        self.res.json = self.api.request(
            path="/networkdevice/search", method="POST", payload=json.dumps(payload)
        )

        self.columns, self.rows = Sort.rows(
            network_device=network_device, pf=self.product_family, data=self.res.json
        )

        if len(self.rows) == 0:
            self.title = f"{self.title}\n\nNo results"

        self.res.raw["rows"] = self.rows
        self.res.cli = Output.table(
            title=self.title,
            columns=self.columns,
            rows=self.rows,
        )
        return self.res
