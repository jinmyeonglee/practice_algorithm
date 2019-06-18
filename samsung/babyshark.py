from collections import deque

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
n = int(input())
m = []
check = [[False] * n for _ in range(n)]

for i in range(n):
    m.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if m[i][j] == 9:
            s = (i, j)

q = deque([])
s_size = 2
eat = 0
ans = 0
q.append((s, 0))
m[s[0]][s[1]] = 0
check[s[0]][s[1]] = True


def canEat(mat, ss):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if 0 < mat[i][j] < ss:
                return True
    return False


while q:
    print(q)
    cur_p, cur_t = q.popleft()
    if not canEat(m, s_size):
        print(cur_t)
        break
    move = False
    for i in range(4):
        y = cur_p[0] + dy[i]
        x = cur_p[1] + dx[i]
        if not (0 <= y < n and 0 <= x < n) or \
                (0 <= y < n and 0 <= x < n and check[y][x]):
            continue
        if m[y][x] < s_size:
            check = [[False] * n for _ in range(n)]
            eat += 1
            m[y][x] = 0
            q = deque([])
            check[y][x] = True
            move = True
            q.append(((y, x), cur_t + 1))
            if eat == s_size:
                s_size += 1
                eat = 0
        elif m[y][x] == 0 or m[y][x] == s_size:
            q.append(((y, x), cur_t + 1))
            check[y][x] = True
            move = True

    if not move:
        print(cur_p, cur_t)
        print(check)
        print(m)
        break






