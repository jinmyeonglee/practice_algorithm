class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preOrder(self):
        s = []
        res = []
        current = self

        while s or current is not None:
            if current is not None:
                s.append(current)
                res.append(current.data)
                print(current.data)
                current = current.left
            else:
                current = s.pop().right

        return res

    def inOrder(self):
        s = []
        res = []
        current = self

        while s or current is not None:
            if current is not None:
                s.append(current)
                current = current.left
            else:
                current = s.pop()
                res.append(current.data)
                print(current.data)
                current = current.right

        return res

    def postOrder(self):
        from collections import deque
        s = []
        res_dq = deque([])
        current = self

        while s or current is not None:
            if current is not None:
                s.append(current)
                res_dq.appendleft(current.data)
                current = current.right
            else:
                current = s.pop().left

        return res_dq


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.inOrder()
print()
root.preOrder()
print()
r = root.postOrder()
print(r)
