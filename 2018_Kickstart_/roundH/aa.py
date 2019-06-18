T = int(input())

for t in range(T):
    n, p = map(int, input().strip().split())
    forbi = []
    for j in range(p):
        forbi.append(input())
    total = 2 ** n
    temp = []
    for k in forbi:
        for h in forbi:
            if k.startswith(h) and len(k) > len(h):
                temp.append(k)

    for j in range(len(forbi)):
        if forbi[j] not in temp:
            total -= 2 ** (n - len(forbi[j]))
    if(total < 0): total = 0
    print("Case #" + str(t+1) + ": " + str(total))
