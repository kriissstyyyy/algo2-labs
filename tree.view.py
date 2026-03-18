import os


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_balanced_bst(values):
    if not values:
        return None
    mid = len(values) // 2
    node = BinaryTree(values[mid])
    node.left = build_balanced_bst(values[:mid])
    node.right = build_balanced_bst(values[mid + 1:])
    return node


def get_height(node):
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


def print_tree(root):
    if root is None:
        print("Дерево порожнє.")
        return

    h = get_height(root)
    cols = 120
    rows = h * 2 + 1
    matrix = [[" " for _ in range(cols)] for _ in range(rows)]

    def place(r, c, txt):
        s = str(txt)
        start = c - len(s) // 2
        for i, char in enumerate(s):
            if 0 <= r < rows and 0 <= start + i < cols:
                matrix[r][start + i] = char

    def draw_branch(r1, c1, r2, c2):
        mr = (r1 + r2) // 2
        mc = (c1 + c2) // 2
        if 0 <= mr < rows and 0 <= mc < cols:
            if c2 < c1:
                matrix[mr][mc] = "╱"
            else:
                matrix[mr][mc] = "╲"

    def fill(node, r, c, offset):
        if not node:
            return
        place(r, c, node.value)

        if node.left:
            child_r = r + 2
            child_c = c - offset
            draw_branch(r, c, child_r, child_c)
            fill(node.left, child_r, child_c, offset // 2)

        if node.right:
            child_r = r + 2
            child_c = c + offset
            draw_branch(r, c, child_r, child_c)
            fill(node.right, child_r, child_c, offset // 2)

    root_r = 0
    root_c = cols // 2
    start_offset = cols // 4

    fill(root, root_r, root_c, start_offset)

    for row in matrix:
        line = "".join(row).rstrip()
        if line:
            print(line)


def read_tree_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    values = list(map(int, content.split()))

    if len(values) > 20:
        print(f"Увага: у файлі {len(values)} чисел, буде використано лише перші 20.")
        values = values[:20]

    if values[0] != 1:
        print("Увага: послідовність має починатися з 1.")

    return sorted(values)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "tree_data.txt")

    if not os.path.exists(filepath):
        print(f"Файл '{filepath}' не знайдено.")
        return

    values = read_tree_from_file(filepath)
    print(f"In-order послідовність: {values}")
    print()

    root = build_balanced_bst(values)

    print("Вигляд дерева зверху вниз:")
    print_tree(root)



if __name__ == "__main__":
    main()