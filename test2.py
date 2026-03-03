import unittest
from lab2 import largest_min_distance

class TestFarmerCows(unittest.TestCase):

    def test_example(self):
        N = 5
        C = 3
        free_sections = [1, 2, 8, 4, 9]
        self.assertEqual(largest_min_distance(N, C, free_sections), 3)

    def test_another(self):
        N = 4
        C = 2
        free_sections = [1, 2, 4, 8]
        self.assertEqual(largest_min_distance(N, C, free_sections), 7)

    def test_min_distance(self):
        N = 6
        C = 3
        free_sections = [1, 2, 3, 4, 5, 6]
        self.assertEqual(largest_min_distance(N, C, free_sections), 2)

    def test_max_distance(self):
        N = 2
        C = 2
        free_sections = [0, 1000000000]
        self.assertEqual(largest_min_distance(N, C, free_sections), 1000000000)

    def test_equal_positions(self):
        N = 3
        C = 3
        free_sections = [1, 5, 9]
        self.assertEqual(largest_min_distance(N, C, free_sections), 4)

if __name__ == "__main__":
    unittest.main()