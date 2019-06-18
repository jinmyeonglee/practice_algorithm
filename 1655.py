from heapq import heappop, heappush
N = int(input())

maxh = []
minh = []
median = int(input())
print(median)
heappush(maxh, (-median, median))
n_max = 1
n_min = 0

for _ in range(N - 1):
    num = int(input())
    if num <= median:
        heappush(maxh, (-num, num))
        n_max += 1
    else:
        heappush(minh, num)
        n_min += 1
    if n_max > n_min + 1:
        _, temp = heappop(maxh)
        heappush(minh, temp)
        median = maxh[0][1]
        n_max -= 1
        n_min += 1
    elif n_min > n_max:
        median = heappop(minh)
        heappush(maxh, (-median, median))
        n_max += 1
        n_min -= 1
    print(median)