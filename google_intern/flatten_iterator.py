from collections import deque


class IF:
    its = deque([])
    ns = deque([])

    def __init__(self, arr):
        self.its = deque(arr)
        for n in range(len(arr)):
            self.ns.append(next(self.its[n]))

    def next(self):
        re = self.ns.popleft()
        it = self.its.popleft()
        try:
            self.ns.append(next(it))
        except StopIteration:
            pass
        else:
            self.its.append(it)
        return re

    def hasNext(self):
        if self.its:
            return True
        else:
            return False


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9, 10]

    a = iter(arr1)
    b = iter(arr2)
    c = iter(arr3)

    arr = [a, b, c]

    itfl = IF(arr)

    while(itfl.hasNext()):
        print(itfl.next())

