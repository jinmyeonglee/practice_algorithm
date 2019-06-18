import itertools
T = int(input())

for t in range(T):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().strip().split()))
    aa = list(itertools.combinations(range(N), 3))
    ans = []
    for i in aa:
        x, y, z = i[0], i[1], i[2]
        if(arr[x] == arr[y] * arr[z]):
            ans.append([x, y, z])
        elif(arr[y] == arr[x] * arr[z]):
            ans.append([x, y, z])
        elif(arr[z] == arr[x] * arr[y]):
            ans.append([x, y, z])

    an_set = set(tuple(i) for i in ans)
    print("Case #%d: %d" %(t+1, len(an_set)))
