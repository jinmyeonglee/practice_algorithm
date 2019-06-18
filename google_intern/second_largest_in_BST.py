class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def second_largest_value(self):
        parent = self
        rightmost = self.right
        if parent.left is None and parent.right is None:
            return None
        while rightmost.right is not None:
            parent = rightmost
            rightmost = rightmost.right
        if rightmost.left is not None:
            return rightmost.left.value
        else:
            return parent.value


if __name__ == "__main__":
    root = BinaryTreeNode(5)
    r = root.insert_right(9)
    r.insert_right(10)
    r.insert_left(8)

    ans = root.second_largest_value()
    print(ans)
