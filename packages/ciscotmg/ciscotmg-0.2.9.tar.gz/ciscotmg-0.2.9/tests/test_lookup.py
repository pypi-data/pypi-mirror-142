import unittest
import ciscotmg


class TestLookup(unittest.TestCase):
    """Lookup test"""

    def __init__(self, methodName: str = ...) -> None:
        """Setup instance"""
        super().__init__(methodName)
        self.svc = ciscotmg.Services()

    def test_lookup_success_pid(self):
        """Lookup for working PID"""
        id = 78
        pid = "SFP-10G-LR-S"
        n = "C9300X-12Y"
        pf = "C9300X"
        res = self.svc.lookup(pid=pid, network_device=None, product_family=None)
        t_in_data = [t for t in res.json["filters"][4]["values"] if t["id"] == id]
        t_id = [
            {
                "id": id,
                "name": pid,
                "count": t_in_data[0]["count"],
                "filterChecked": True,
            }
        ]
        n_in_data = [p for p in res.raw["rows"] if p[0] == n]

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(t_id, t_in_data)
        self.assertEqual(1, len(n_in_data))
        self.assertEqual(pf, n_in_data[0][1])
        self.assertIn("productFamily", res.json["networkDevices"][0])

    def test_lookup_success_pid_with_pf(self):
        """Lookup for working PID"""
        id = 78
        pid = "SFP-10G-LR-S"
        n = "C9300X-12Y"
        pf = "C9300X"
        res = self.svc.lookup(pid=pid, network_device=None, product_family=pf)
        t_in_data = [t for t in res.json["filters"][4]["values"] if t["id"] == id]
        t_id = [
            {
                "id": id,
                "name": pid,
                "count": t_in_data[0]["count"],
                "filterChecked": True,
            }
        ]
        n_in_data = [p for p in res.raw["rows"] if p[0] == n]

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(t_id, t_in_data)
        self.assertEqual(1, len(n_in_data))
        self.assertEqual(pf, n_in_data[0][1])
        self.assertIn("productFamily", res.json["networkDevices"][0])

    def test_lookup_suggestion_pid(self):
        """Lookup with no exact match and receive suggestion PIDs"""
        pid = "SFP-10G"
        suggestion = {
            "rows": [
                ["SFP-10G-SR", "Yes", "No"],
                ["SFP-10G-SR-S", "Yes", "No"],
                ["SFP-10G-LRM", "Yes", "No"],
            ]
        }
        res = self.svc.lookup(pid=pid, network_device=None, product_family=None)

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(suggestion, res.raw)

    def test_lookup_failed(self):
        """Lookup failed for pid"""
        pid = "a7c06ea4-5fe1-4bd7-8be6-ciscotmg-py-test"
        res = self.svc.lookup(pid=pid, network_device=None, product_family=None)

        self.assertIsInstance(res.json, dict)
        self.assertEqual(0, len(res.json))
        self.assertEqual(0, len(res.raw))

    def test_lookup_success_pid_network_device(self):
        """Search a working PID"""
        id = 193
        pid = "C9500-32C"
        n_id = [{"id": id, "name": pid, "count": 98, "filterChecked": True}]
        res = self.svc.lookup(pid=pid, network_device=True, product_family=None)
        n_in_data = [n for n in res.json["filters"][7]["values"] if n["id"] == id]

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(n_id, n_in_data)
        self.assertNotEqual(pid, res.raw["rows"][0][0])
        self.assertEqual(res.json["networkDevices"][0]["productFamily"], "C9500")

    def test_lookup_success_pid_network_device_with_pf(self):
        """Search a working PID with Product Family filter"""
        id = 193
        pid = "C9500-32C"
        pf = "C9500"
        n_id = [{"id": id, "name": pid, "count": 98, "filterChecked": True}]
        res = self.svc.lookup(pid=pid, network_device=True, product_family=pf)
        n_in_data = [n for n in res.json["filters"][7]["values"] if n["id"] == id]

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(n_id, n_in_data)
        self.assertNotEqual(pid, res.raw["rows"][0][0])
        self.assertEqual(res.json["networkDevices"][0]["productFamily"], pf)

    def test_lookup_failed_transceiver_network_device(self):
        """Search a transceiver PID with Network Device flag"""
        id = 78
        pid = "SFP-10G-LR-S"
        t_id = {"transceiverProductID": [{"id": id, "name": pid}]}
        res = self.svc.lookup(pid=pid, network_device=True, product_family=None)

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(t_id, res.json)
        self.assertEqual(pid, res.raw["rows"][0][0])
        self.assertEqual("Yes", res.raw["rows"][0][1])
        self.assertEqual("No", res.raw["rows"][0][2])

    def test_lookup_failed_transceiver_with_network_device_and_pf(self):
        """Search a transceiver PID with Network Device flag and Product Family filter"""
        id = 78
        pid = "SFP-10G-LR-S"
        pf = "C9500"
        t_id = {"transceiverProductID": [{"id": id, "name": pid}]}
        res = self.svc.lookup(pid=pid, network_device=True, product_family=pf)

        self.assertIsInstance(res.json, dict)
        self.assertNotEqual(0, len(res.json))
        self.assertEqual(t_id, res.json)
        self.assertEqual(pid, res.raw["rows"][0][0])
        self.assertEqual("Yes", res.raw["rows"][0][1])
        self.assertEqual("No", res.raw["rows"][0][2])

    def test_lookup_failed_pid_missing_network_device(self):
        """Search a Network PID without Network Device flag"""
        id = 193
        pid = "C9500-32C"
        n_id = {"networkDeviceProductID": [{"id": id, "name": pid}]}
        res = self.svc.lookup(pid=pid, network_device=False, product_family=None)
        self.assertNotEqual(0, len(res.json))
        self.assertIsInstance(res.json, dict)
        self.assertEqual(n_id, res.json)
        self.assertEqual(pid, res.raw["rows"][0][0])

    def test_lookup_unique_network_device_with_network_device(self):
        """Search a Network PID that has to be exact with Network Device flag"""
        id = 5182
        pid = "C9300X-48HXN"
        n_id = {"networkDeviceProductID": [{"id": id, "name": pid}]}
        res = self.svc.lookup(pid=pid, network_device=False, product_family=None)
        self.assertNotEqual(0, len(res.json))
        self.assertIsInstance(res.json, dict)
        self.assertEqual(n_id, res.json)
        self.assertEqual(pid, res.raw["rows"][0][0])


if __name__ == "__main__":
    unittest.main(verbosity=3)
