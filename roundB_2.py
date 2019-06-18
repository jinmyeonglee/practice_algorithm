import collections
import copy

T = int(input())

for t in range(1, T + 1):
    ans = 0
    N, S = map(int, input().split())
    x = list(map(int, input().split()))
    arr = [collections.defaultdict(lambda: 0)]
    for i in range(1, N + 1):
        pre = copy.deepcopy(arr[i - 1])
        pre[x[i - 1]] += 1
        arr.append(pre)

    for l in range(N):
        for r in range(l + 1, N + 1):
            L, R = arr[l - 1], copy.deepcopy(arr[r])
            temp = 0
            for key, value in L.items():
                R[key] -= value
            for value in R.values():
                if 0 < value <= S:
                    temp += value
            ans = max(ans, temp)
    print("Case #%d: %d" % (t, ans))
