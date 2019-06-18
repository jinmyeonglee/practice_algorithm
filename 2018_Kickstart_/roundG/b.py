from segment_tree import *
T = int(input())

for t in range(T):
    N, Q = map(int, input().strip().split())

    x = [0] * (N + 1)
    y = [0] * (N + 1)
    z = [0] * (Q + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    K = [0] * (Q + 1)
    Sum = 0
    x[1], x[2], A1, B1, C1, M1 = map(int, input().strip().split())
    y[1], y[2], A2, B2, C2, M2 = map(int, input().strip().split())
    z[1], z[2], A3, B3, C3, M3 = map(int, input().strip().split())
    total_num = 0
    for i in range(3, N + 1):
        x[i] = (A1 * x[i-1] + B1 * x[i-2] + C1) % M1
        y[i] = (A2 * y[i-1] + B2 * y[i-2] + C2) % M2
    for i in range(3, Q + 1):
        z[i] = (A3 * z[i-1] + B3 * z[i-2] + C3) % M3
    for i in range(1, N + 1):
        L[i] = min(x[i], y[i]) + 1
        R[i] = max(x[i], y[i]) + 1
        total_num += R[i] - L[i] + 1
    for i in range(1, Q + 1):
        K[i] = z[i] + 1

    seg_tree = SegmentTree([0]*(total_num + 1))
