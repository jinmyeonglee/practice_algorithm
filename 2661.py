N = int(input())
ans = "1"*80
can = ["1", "2", "3"]

def check(num_str):
    length = len(num_str)
    for win in range(1, length // 2 + 1):
        for i in range(length - win):
            if num_str[i: i+win] == num_str[i+win: 2*win+i]:
                return False
    return True

i = 1
while(i != N):
    for c in can:
        temp = ans + c
        if check(temp):
            ans = temp
            break

    i += 1
for i in range(N - 1):
    for c in can:
        temp = ans + c
        if check(temp):
            ans = temp
            break
print(ans)
