class Sort:
    """Sorting orders for data"""

    @classmethod
    def rows(cls, network_device, pf, data) -> list:
        """Sorts rows based on type"""
        cls.pf = pf
        cls.data = data
        if network_device:
            return cls.network_device()
        else:
            return cls.transceiver()

    @classmethod
    def network_device(cls) -> list:
        """Sort Network Device"""
        columns = [
            "PID",
            "Product Family",
            "Data Rate",
            "Form",
            "Max. Reach",
            "Cable Type",
            "Media",
            "Connector Type",
            "Type",
            "Case Temp",
            "DOM HW Capable",
            "OS Minimum",
            "DOM SW",
        ]
        rows = []
        for pids in cls.data["networkDevices"]:
            for p in pids["networkAndTransceiverCompatibility"]:
                for t in p["transceivers"]:
                    t["softReleaseMinVer"] = cls.check_release_notes(
                        t["softReleaseMinVer"]
                    )
                    t["digitalDiagnostic"] = cls.check_dom_support(
                        t["digitalDiagnostic"]
                    )
                    t["temperatureRange"] = cls.add_newline_temperature(
                        t["temperatureRange"]
                    )

                    row = [
                        t["productId"],
                        pids["productFamily"],
                        t["dataRate"],
                        t["formFactor"],
                        t["reach"],
                        t["cableType"],
                        t["media"],
                        t["connectorType"],
                        t["type"],
                        t["temperatureRange"],
                        t["digitalDiagnostic"],
                        t["softReleaseMinVer"],
                        t["softReleaseDOM"],
                    ]

                    if isinstance(cls.pf, list):
                        if pids["productFamily"] in cls.pf:
                            rows.append(row)
                    else:
                        rows.append(row)
        return columns, rows

    @classmethod
    def transceiver(cls) -> list:
        """Sort Transceiver"""
        columns = [
            "PID",
            "Product Family",
            "Data Rate",
            "Form",
            "Max. Reach",
            "Cable Type",
            "Media",
            "Connector Type",
            "Type",
            "Case Temp",
            "DOM HW Capable",
            "OS Minimum",
            "DOM SW",
        ]
        rows = []
        for pids in cls.data["networkDevices"]:
            for p in pids["networkAndTransceiverCompatibility"]:
                for t in p["transceivers"]:
                    t["softReleaseMinVer"] = cls.check_release_notes(
                        t["softReleaseMinVer"]
                    )
                    t["digitalDiagnostic"] = cls.check_dom_support(
                        t["digitalDiagnostic"]
                    )
                    t["temperatureRange"] = cls.add_newline_temperature(
                        t["temperatureRange"]
                    )

                    row = [
                        p["productId"],
                        pids["productFamily"],
                        t["dataRate"],
                        t["formFactor"],
                        t["reach"],
                        t["cableType"],
                        t["media"],
                        t["connectorType"],
                        t["type"],
                        t["temperatureRange"],
                        t["digitalDiagnostic"],
                        t["softReleaseMinVer"],
                        t["softReleaseDOM"],
                    ]

                    if isinstance(cls.pf, list):
                        if pids["productFamily"] in cls.pf:
                            rows.append(row)
                    else:
                        rows.append(row)
        return columns, rows

    @classmethod
    def check_release_notes(cls, data) -> str:
        """Remove long text in table"""
        if "please" in data.lower():
            return "Check RN"
        return data

    @classmethod
    def check_dom_support(cls, data) -> str:
        """Convert text to Yes/No"""
        if data == "Y":
            return "Yes"
        else:
            return "No"

    @classmethod
    def add_newline_temperature(cls, data) -> str:
        """Add /n instead of /"""
        if "/" in data:
            res = ""
            data = data.split("/ ")
            for i, d in enumerate(data):
                if i == 0:
                    res = f"{d}"
                else:
                    res = f"{res}\n{d}"
            return res
        return data
