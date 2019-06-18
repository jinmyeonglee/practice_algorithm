import itertools
T = int(input())

for t in range(T):
    n = int(input())
    c_x = []
    c_y = []
    for i in range(n):
        x, y = map(int, input().split())
        c_x.append(x)
        c_y.append(y)
    cb = list(itertools.combinations(range(n), 2))
    max = 0
    coor = ()
    for i in cb:
        d = (c_x[i[0]] - c_x[i[1]])**2 + (c_y[i[0]] - c_y[i[1]])**2
        if(d > max):
            max = d
            coor = i

    print(c_x[coor[0]], c_y[coor[0]], c_x[coor[1]], c_y[coor[1]])
