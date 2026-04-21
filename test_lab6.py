import unittest
from lab6 import find_unreachable_cities

class TestGasDelivery(unittest.TestCase):
    def test_all_reachable(self):
        cities = ["Lviv", "Stryi"]
        storages = ["Storage_1"]
        pipes = [["Storage_1", "Lviv"], ["Lviv", "Stryi"]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), [])

    def test_unreachable_city(self):
        cities = ["Lviv", "Stryi", "Dolyna"]
        storages = ["Storage_1"]
        pipes = [["Storage_1", "Lviv"], ["Lviv", "Stryi"]]
        expected = [["Storage_1", ["Dolyna"]]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), expected)

    def test_disconnected_storage(self):
        cities = ["Lviv"]
        storages = ["Storage_1"]
        pipes = []
        expected = [["Storage_1", ["Lviv"]]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), expected)

    def test_transit_path(self):
        cities = ["City_A", "City_B", "City_C"]
        storages = ["Storage_X"]
        pipes = [["Storage_X", "City_A"], ["City_A", "City_B"], ["City_B", "City_C"]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), [])

if __name__ == "__main__":
    unittest.main()