import itertools
import sys
from operator import itemgetter
import copy

T = int(input())
list_ans = []

def score(p, req):
    sc = 0

    for i in req:
        for k in range(len(i)):
            if(i[k] != p[k]):
                sc += 1
    return sc

for t in range(T):
    n, m, p = map(int, input().strip().split())
    req = []
    forbidden = []
    profile = []
    for i in range(n):
        req.append(list(input()))
    for i in range(m):
        forbidden.append(list(input()))
    for i in range(p):
        cnt_1 = 0
        cnt_0 = 0
        for j in range(n):
            if(req[j][i] == "1"): cnt_1 += 1
            elif(req[j][i] == "0"): cnt_0 += 1
        if(cnt_0 > cnt_1): profile.append(("0", cnt_0))
        elif(cnt_0 < cnt_1): profile.append(("1", cnt_1))

    profile.sort(key=itemgetter(1))
    check = list(map(lambda x: x[0], profile))
    if(check not in forbidden):
        print(score(check, req))
        sys.exit()

    toggle = 1
    check = list(map(lambda x: x[0], profile))
    while(True):
        temp = copy.deepcopy(check)
        for to in range(toggle):
            temp[to] = "1" if temp[to] == "0" else "0"
        if(temp not in forbidden):
            print(score(temp, req))
            break
        else:
            temp = copy.deepcopy(check)
        toggle += 1

    # list_ans.append(min)
    # print("Case #%d: %d" %(t+1, min))
# for t in range(T):
#     print("Case #%d: %d" %(t+1, list_ans[t]))
