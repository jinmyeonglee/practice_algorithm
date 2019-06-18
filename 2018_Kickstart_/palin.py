import itertools
al = "abcdefghijklmnopqrstuvwxyz"

T = int(input())

for t in range(T):
    L, N, K = map(int, input().strip().split())
    ch = al[0:L]
    arr = []
    for i in range(1, N+1):
        temp = list(map(list, list(itertools.permutations(ch*N, i))))
        for k in temp:
            str = "".join(k)
            if(str == str[::-1]):
                arr.append(str)
    arr = set(arr)
    arr = list(arr)
    arr.sort()

    try: print("Case #%d: %d" %( t+1, len(arr[K+1])))
    except: print("Case #%d: 0"%(t+1))
