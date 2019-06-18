class Trie():

T = int(input())

for t in range(T):
    n, m = map(int, input().strip().split())

    str = input()
    marker = input()
    ex = set([marker])
    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            temp = ""
            if(i == 0):
                temp = marker[j::-1] + marker[j+1:]
            else:
                temp = marker[:i] + marker[j:i-1:-1] + marker[j+1:]
            ex.add(temp)
    for i in range(n - m + 1):
        if(str[i:i+m] in ex):
            ans += 1
    print(ans)
