class Dot():
    time = 0
    gas = 0
    dir = 0
    def __init__(self):
        self.time = 0
        self.gas = 0
        self.dir = 0

T = int(input())

for t in range(T):
    ver = []
    hor = []
    dots = []
    M, N, L, G = map(int, input().strip().split())
    for i in range(M):
        ver.append(list(map(int, input().strip().split())))
        dots.append([Dot() for x in range(N)])
    for i in range(M - 1):
        hor.append(list(map(int, input().strip().split())))
    sum_g = 0
    sum_t = 0
    for i in range(N-1):
        sum_g += ver[0][i]
        sum_t += L
        dots[0][i+1].gas, dots[0][i+1].time, dots[0][i+1].dir = sum_g, sum_t, 1
    sum_g = 0
    sum_t = 0
    for i in range(M-1):
        sum_g += hor[i][0]
        sum_t += L
        dots[i+1][0].gas, dots[i+1][0].time, dots[i+1][0].dir = sum_g, sum_t, 2
    for i in range(1, M):
        for j in range(1, N):
            up = dots[i-1][j]
            side = dots[i][j-1]
            if(hor[i-1][j] + up.gas > G and ver[i][j-1] + side.gas > G):
                dots[i][j].gas = 10000000
                dots[i][j].time = 10000000
            elif(hor[i-1][j] + up.gas > G):
                dots[i][j].gas = side.gas + ver[i][j-1]
                dots[i][j].time = side.time + L
                dots[i][j].dir = 1
                if(side.dir == 2): dots[i][j].time += 1
            elif(ver[i][j-1] + side.gas > G):
                dots[i][j].gas = up.gas + hor[i-1][j]
                dots[i][j].time = up.time + L
                dots[i][j].dir = 2
                if(up.dir == 1): dots[i][j].time += 1
            else:
                up_time = up.time + L
                side_time = side.time + L
                if(up.dir == 1): up_time += 1
                if(side.dir == 2): side_time += 1
                if(up_time > side_time):
                    dots[i][j].gas = side.gas + ver[i][j-1]
                    dots[i][j].time = side.time + L
                    dots[i][j].dir = 1
                    if(side.dir == 2): dots[i][j].time += 1
                else:
                    dots[i][j].gas = up.gas + hor[i-1][j]
                    dots[i][j].time = up.time + L
                    dots[i][j].dir = 2
                    if(up.dir == 1): dots[i][j].time += 1

    for i in range(M):
        for j in range(N):
            print(dots[i][j].time, end=" ")
        print()
