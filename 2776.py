import bisect
T = 3

for t in range(T):
    N = int(input())
    arr_1 = list(map(int, input().strip().split()))
    M = int(input())
    arr_2 = list(map(int, input().strip().split()))
    arr_1.sort()
    for i in arr_2:
        index = bisect.bisect_left(arr_1, i)
        if(index != len(arr_1) and arr_1[index] == i): print("1")
        else: print("0")
