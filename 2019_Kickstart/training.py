T = int(input())

for t in range(1, T + 1):
    n, p = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    min_v = 10000 * p

    for i in range(n - p + 1):
        window_sum = 0
        m = s[i + p - 1]
        for j in range(i, i + p):
            window_sum += m - s[j]
        if min_v >= window_sum:
            min_v = window_sum

    print("Case #%d: %d" % (t, min_v))

