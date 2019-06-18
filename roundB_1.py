import copy
import collections

T = int(input())

for t in range(1, T + 1):
    ans = 0
    N, Q = map(int, input().split())
    s = input()
    arr = [collections.defaultdict(lambda: 0)]
    for i in range(1, len(s) + 1):
        pre = copy.deepcopy(arr[i - 1])
        pre[s[i - 1]] += 1
        arr.append(pre)
    for q in range(Q):
        l, r = map(int, input().split())
        L, R = arr[l - 1], copy.deepcopy(arr[r])
        for key, value in L.items():
            R[key] -= value
        check = 0
        for value in R.values():
            if value % 2 == 1:
                check += 1
        if check == 1 or check == 0:
            ans += 1
    print("Case #%d: %d" % (t, ans))
