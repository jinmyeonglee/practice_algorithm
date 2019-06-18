S = input()

dp = [[False] * len(S) for _ in range(len(S))]

for i in range(len(S)):
    for j in range(len(S)):
        if i == j:
            dp[i][j] = True
        elif j == i + 1 and S[j] == S[i]:
            dp[i][j] = True

for j in range(len(S)):
    for i in range(len(S)):
        if 0 <= i+1 < len(S) and 0 <= j-1 < len(S) and dp[i+1][j-1] and S[i] == S[j]:
            dp[i][j] = True

max_v = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        if dp[i][j] and j - i + 1 > max_v:
            max_v = j - i + 1

print(max_v)
