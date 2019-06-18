from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = []
dq = deque([])

for index, item in enumerate(a):
    while dq and dq[-1][1] > item:
        dq.pop()
    dq.append((index, item))
    if not index - l < dq[0][0] <= index:
        dq.popleft()
    d.append(dq[0][1])

for item in d:
    print(item, end=" ")
