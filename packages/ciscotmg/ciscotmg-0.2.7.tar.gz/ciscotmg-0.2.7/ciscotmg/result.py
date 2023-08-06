import json


class Result:
    """Python Attributes as results"""

    def __init__(self) -> None:
        self.cli = None
        self.json = json.dumps(None)
