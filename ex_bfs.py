# definition of variables
n = 0
arr = [] # double list of char
dy = [1, -1, 0, 0] # for changing direction
dx = [0, 0, 1, -1]
visited = [] # for marking visited or not

# definition of functions
def dfs(y, x):
    global n, arr, visited
    mark = arr[y][x]
    for i in range(4):
        if(y+dy[i] < 0 or y+dy[i] >= n or x+dx[i] < 0 or x+dx[i] >= n):
            continue
        if(arr[y+dy[i]][x+dx[i]] == mark and visited[y+dy[i]][x+dx[i]] == False):
            visited[y+dy[i]][x+dx[i]] = True
            dfs(y+dy[i], x+dx[i])

def solution():
    global n, arr, visited

    cnt = 0
    for i in range(n):
        for j in range(n):
            if(visited[i][j] == False):
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    return cnt
# start
if __name__ == "__main__":
    n = int(input()) # get the size of grid
    visited = [[False]*n for i in range(n)]
    for i in range(n): # get the grid
        arr.append(list(str(input())))

    normal = solution()

    for i in range(n):
        for j in range(n):
            if(arr[i][j] == "R"):
                arr[i][j] = "G"

    visited = [[False]*n for i in range(n)]
    abnoraml = solution()
    print(normal, abnoraml)
