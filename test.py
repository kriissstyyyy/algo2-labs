import unittest
from lab1 import find_kth_largest

class TestFindKthLargest(unittest.TestCase):

    def setUp(self):
        self.array = [4, 81, 17, 55, 3, 29, 66, 12]

    def test_k1(self):
        result_value, result_pos = find_kth_largest(self.array, 1)
        self.assertEqual(result_value, 81)
        self.assertEqual(result_pos, 1)

    def test_k3(self):
        result_value, result_pos = find_kth_largest(self.array, 3)
        self.assertEqual(result_value, 55)
        self.assertEqual(result_pos, 3)

    def test_last(self):
        result_value, result_pos = find_kth_largest(self.array, 8)
        self.assertEqual(result_value, 3)
        self.assertEqual(result_pos, 4)

    def test_negatives(self):
        result_value, result_pos = find_kth_largest([-10, -3, -7, -1], 2)
        self.assertEqual(result_value, -3)
        self.assertEqual(result_pos, 1)

    def test_mixed(self):
        result_value, result_pos = find_kth_largest([-5, 0, 8, -2, 3], 3)
        self.assertEqual(result_value, 0)
        self.assertEqual(result_pos, 1)

    def test_single_element(self):
        result_value, result_pos = find_kth_largest([42], 1)
        self.assertEqual(result_value, 42)
        self.assertEqual(result_pos, 0)

    def test_invalid_k_zero(self):
        with self.assertRaises(ValueError):
            find_kth_largest(self.array, 0)

    def test_invalid_k_too_big(self):
        with self.assertRaises(ValueError):
            find_kth_largest(self.array, 99)

if __name__ == "__main__":
    unittest.main()