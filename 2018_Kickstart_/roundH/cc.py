import math
fac = math.factorial
T = int(input())

for t in range(T):
    n, m = map(int, input().strip().split())
    ans = fac(2*n) - ((fac(2*n - 1) * 2)*m) + fac(m+(n-1)) * (2**m)
    print("Case #" + str(t+1) + ": " +str(ans))
