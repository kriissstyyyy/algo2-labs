import unittest
from lab4 import RedBlackPriorityQueue


class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Low", 5)
        self.pq.insert("High", 15)
        self.pq.insert("Mid", 10)

        value, priority = self.pq.peek()
        self.assertEqual(value, "High")
        self.assertEqual(priority, 15)

    def test_extract_max_order(self):
        self.pq.insert("A", 10)
        self.pq.insert("B", 30)
        self.pq.insert("C", 20)

        self.assertEqual(self.pq.extract_max(), ("B", 30))
        self.assertEqual(self.pq.extract_max(), ("C", 20))
        self.assertEqual(self.pq.extract_max(), ("A", 10))

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.extract_max())

    def test_multiple_same_priorities(self):
        self.pq.insert("Task1", 10)
        self.pq.insert("Task2", 10)

        val1, prio1 = self.pq.extract_max()
        val2, prio2 = self.pq.extract_max()

        self.assertEqual(prio1, 10)
        self.assertEqual(prio2, 10)
        self.assertIsNone(self.pq.peek())

    def test_large_scale(self):
        for i in range(1, 101):
            self.pq.insert(f"Task{i}", i)

        val, prio = self.pq.peek()
        self.assertEqual(prio, 100)
        self.assertEqual(val, "Task100")


if __name__ == "__main__":
    unittest.main()