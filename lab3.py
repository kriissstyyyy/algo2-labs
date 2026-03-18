class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def _diameter_helper(self, node):
        if node is None:
            return 0, 0

        left_diameter, left_height = self._diameter_helper(node.left)
        right_diameter, right_height = self._diameter_helper(node.right)

        diameter_through_node = left_height + right_height
        max_diameter = max(diameter_through_node, left_diameter, right_diameter)
        current_height = 1 + max(left_height, right_height)

        return max_diameter, current_height

    def binary_tree_diameter(self):
        diameter, _ = self._diameter_helper(self)
        return diameter

    @staticmethod
    def get_diameter(tree: 'BinaryTree') -> int:
        if tree is None:
            return 0
        return tree.binary_tree_diameter()
    
