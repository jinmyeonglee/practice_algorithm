from collections import deque
T = int(input())
x_ans = []
for t in range(T):
    n, k = map(int, input().strip().split())
    yog = list(map(int, input().strip().split()))

    yog.sort()
    yog = deque(yog)
    ans = 0
    day = 0
    for i in range(yog[-1] +  1):
        if(len(yog) == 0):
            break
        j = 0
        while(j < k):
            if(len(yog) == 0):
                break
            if(yog[0] > day):
                yog.popleft()
                ans += 1
                j += 1
            else:
                yog.popleft()
        day += 1
    x_ans.append(ans)

for t in range(T):
    print("Case #%d: %d" %(t+1, x_ans[t]))
