N = int(input())

grid_r = [[False] * N for _ in range(N)]
grid = []
for i in range(N):
    grid.append(list(list(input())))


def rec(i, j, step):
    if step != 1 and grid[i][j + step]:
        return "(" + rec(i, j, step // 2) + rec(i, j + step, step // 2) + rec(i + step, j, step // 2) + rec(i + step, j + step, step // 2) + ")"
    if grid[i][j + step] is None:
        return grid[i][j]
    if step == 1:
        return "(" + grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1] + ")"
    return "E"


# main flow will start from here.
k = 1
i, j = 0, 0
while(k < N):
    while(i < N - k):
        while(j < N - k):
            if (k == 1) or (k > 1 and grid_r[i][j] and grid_r[i+k][j] and grid_r[i+k][j+k]):
                if grid[i][j] == grid[i][j+k] and grid[i][j] == grid[i+k][j] and grid[i][j] == grid[i+k][j+k]:
                    grid[i][j+k] = grid[i+k][j] = grid[i+k][j+k] = None
                    grid_r[i][j] = True
            j += k * 2
        i += k * 2
        j = 0
    k *= 2
    i = 0


if N == 1:
    result = "(" + grid[0][0] + ")"
else:
    result = rec(0, 0, N // 2)
print(result)