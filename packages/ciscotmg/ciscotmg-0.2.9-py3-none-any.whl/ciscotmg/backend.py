import requests
from .meta import Meta


class API:
    """HTTP API Request to Cisco TMG API"""

    def __init__(self) -> None:
        """Default settings"""
        self.url = "https://tmgmatrix.cisco.com/public/api"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "user-agent": f"{Meta.__title__}-py/v{Meta.__version__}",
        }

    def request(self, path, method, payload=None) -> dict:
        """HTTP requests"""
        if method == "GET":
            response = requests.request(
                method, f"{self.url}{path}", headers=self.headers
            )
        if method == "POST":
            response = requests.request(
                method, f"{self.url}{path}", headers=self.headers, data=payload
            )
        response.raise_for_status()
        try:
            response.json()
        except requests.JSONDecodeError as error_msg:
            raise requests.JSONDecodeError(
                f"Can't decode response from {self.url} - {error_msg}"
            )
        return response.json()

    def check_latest_pypi_version(self) -> str:
        """Check latest version published on pypi"""
        self.url = "https://pypi.python.org/pypi/ciscotmg/json"
        res = self.request(path="", method="GET")
        return res["info"]["version"]
