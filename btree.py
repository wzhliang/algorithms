class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "N({}:[{},{}])".format(self.key,
            self.left.value if self.left else -1,
            self.right.value if self.right else -1)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, root, key, value):
        if root is None:
            root = Node(key, value)
            self.size += 1
            return root
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value
        return root

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def __len__(self):
        return self.size

    def _get(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root.value
        elif key < root.key:
            return self._get(root.left, key)
        else:
            return self._get(root.right, key)

    def get(self, key):
        return self._get(self.root, key)


if __name__ == '__main__':
    bt = BinaryTree()
    data = [49, 5, 12, 47, 51, 60, 42, 94, 53, 85]
    for d in data:
        bt.insert(d, "Element {}".format(d))
    assert(len(bt) == len(data))
    for d in data:
        print("{}: {}".format(d, bt.get(d)))
        assert(bt.get(d) == "Element {}".format(d))
