from collections import deque


N = int(input())

arr = []

for _ in range(N):
    s, t = map(int, list(input().split()))
    arr.append((s, t))

res = 0
for _ in range(N):
    cows = deque([arr.pop()])
    # while(cows[-1][0])


