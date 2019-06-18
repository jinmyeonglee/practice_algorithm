T = int(input())

for t in range(T):
    m, n = map(int, input().strip().split())
    print("1")
    if m % 2 == 0: # m is odd number
        for i in range(m):
            if(i % 2 == 0):
                for j in range(n):
                    print("(%d,%d)" %(i, j))
            else:
                for j in range(n - 1, -1, -1):
                    print("(%d,%d)" %(i, j))
    else:
        for i in range(n):
            print("(0,%d)" %(i))
        for i in range(1, m):
            if(i % 2 == 0):
                for j in range(1, n):
                    print("(%d,%d)" %(i, j))
            else:
                for j in range(n - 1, 0, -1):
                    print("(%d,%d)" %(i, j))
        for i in range(m-1, 0, -1):
            print("(%d,0)" %(i))
