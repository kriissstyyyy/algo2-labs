class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = 'red'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL_LEAF = Node(None, None)
        self.NIL_LEAF.color = 'black'
        self.root = self.NIL_LEAF

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        self._insert_node(new_node)
        self._fix_insert(new_node)

    def extract_max(self):
        node = self._find_max_node()
        if node == self.NIL_LEAF:
            return None
        res_value, res_priority = node.value, node.priority
        self._delete_node(node)
        return res_value, res_priority

    def peek(self):
        node = self._find_max_node()
        if node != self.NIL_LEAF:
            return node.value, node.priority
        return None

    def _insert_node(self, node):
        y = None
        x = self.root
        while x != self.NIL_LEAF:
            y = x
            if node.priority >= x.priority:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.priority >= y.priority:
            y.left = node
        else:
            y.right = node

    def _find_max_node(self):
        current = self.root
        if current == self.NIL_LEAF:
            return self.NIL_LEAF
        while current.left != self.NIL_LEAF:
            current = current.left
        return current

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def _fix_insert(self, k):
        while k.parent and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL_LEAF:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL_LEAF:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self._right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 'black' and s.left.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self._left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def _minimum(self, node):
        while node.right != self.NIL_LEAF:
            node = node.right
        return node

if __name__ == "__main__":
    pq = RedBlackPriorityQueue()
    pq.insert("Task Low", 5)
    pq.insert("Task High", 15)
    pq.insert("Task Mid", 10)
    print("Peek Max:", pq.peek())
    print("Extract Max:", pq.extract_max())
    print("Next Max:", pq.peek())
