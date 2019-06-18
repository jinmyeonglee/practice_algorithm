N = int(input())
pool = []
for _ in range(N):
    row = input().split()
    pool.append((int(row[0]), int(row[1])))
    pool.sort(key=lambda x: x[1])

cnt = 1
i = 0
while i < N:
    for j in range(i, N):
        if pool[j][0] >= pool[i][1]:
            i = j + 1
            cnt += 1
            break
    if j == N - 1:
        break

if N == 1:
    cnt = 1
print(cnt)