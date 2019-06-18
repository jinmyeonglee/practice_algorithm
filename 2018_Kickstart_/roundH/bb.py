T = int(input())

for t in range(T):
    n = int(input())
    scores = list(map(int, list(input())))
    can = 0
    if n % 2 == 0:
        can = n // 2
    else:
        can = n // 2 + 1
    sums = []
    for i in range(n):
        sums.append(sum(scores[i:i+can]))
    print("Case #" + str(t+1) + ": " +str(max(sums)))
