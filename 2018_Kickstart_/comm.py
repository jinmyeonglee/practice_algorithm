import itertools
from collections import Counter
import bisect
T = int(input())
list_ans = []
for t in range(T):
    cnt = 0
    L = int(input())
    A = input()
    B = input()
    A_sub = []
    B_sub = []
    myset = set()
    num = 0
    for i in range(L):
        for j in range(i+1, L+1):
            A_sub.append(A[i:j])
            B_sub.append(B[i:j])
            num += 1

    check = False
    A_sub.sort()
    B_sub.sort()
    for i in A_sub:
        index = bisect.bisect_left(B_sub, i)
        if(index != num and B_sub[index] == i):
            cnt += 1
            continue
        for j in B_sub:
            if(Counter(i) == Counter(j)):
                check = True
                cnt += 1
                break
            if(check == True):
                check = False
                continue
    list_ans.append(cnt)
for t in range(T):
    print("Case #%d: %d" %(t+1, list_ans[t]))
