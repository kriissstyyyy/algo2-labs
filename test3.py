import unittest
from lab3 import BinaryTree


class TestBinaryTreeDiameter(unittest.TestCase):

    def test_example_from_task(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)
        self.assertEqual(BinaryTree.get_diameter(root), 6)

    def test_single_node(self):
        root = BinaryTree(1)
        self.assertEqual(BinaryTree.get_diameter(root), 0)

    def test_two_nodes(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        self.assertEqual(BinaryTree.get_diameter(root), 1)

    def test_three_nodes_line(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertEqual(BinaryTree.get_diameter(root), 2)

    def test_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertEqual(BinaryTree.get_diameter(root), 3)

    def test_diameter_not_through_root(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(5)
        root.left.right.right = BinaryTree(6)
        self.assertEqual(BinaryTree.get_diameter(root), 4)

    def test_right_skewed_tree(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)
        root.right.right.right = BinaryTree(4)
        self.assertEqual(BinaryTree.get_diameter(root), 3)

    def test_none_tree(self):
        self.assertEqual(BinaryTree.get_diameter(None), 0)

    def test_method_call_from_instance(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(root.binary_tree_diameter(), 3)


if __name__ == "__main__":
    unittest.main()