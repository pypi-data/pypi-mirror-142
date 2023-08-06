import unittest
import ciscotmg


class TestSearch(unittest.TestCase):
    """Search test"""

    def __init__(self, methodName: str = ...) -> None:
        """Setup instance"""
        super().__init__(methodName)
        self.svc = ciscotmg.Services()

    def test_search_success_one_pid(self):
        """Search a working PID"""
        id = 78
        pid = "SFP-10G-LR-S"
        res = self.svc.search(pid=pid)

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertIsInstance(res.json["transceiverProductID"], list)
        self.assertIn("id", res.json["transceiverProductID"][0])
        self.assertIn("name", res.json["transceiverProductID"][0])
        self.assertEqual(res.json["transceiverProductID"][0]["id"], id)
        self.assertEqual(res.json["transceiverProductID"][0]["name"], pid)

    def test_search_success_multi_pid(self):
        """Search for multi working PIDs"""
        pid = "SFP-10G"
        res = self.svc.search(pid=pid)

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertIsInstance(res.json["transceiverProductID"], list)
        for p in res.json["transceiverProductID"]:
            self.assertIsInstance(p, dict)
            self.assertIn("id", p)
            self.assertIn("name", p)

    def test_search_failed(self):
        """Search for non-working PID"""
        pid = "a7c06ea4-5fe1-4bd7-8be6-ciscotmg-py-test"
        res = self.svc.search(pid=pid)

        self.assertIsInstance(res.json, dict)
        self.assertEqual(0, len(res.json))


if __name__ == "__main__":
    unittest.main(verbosity=3)
