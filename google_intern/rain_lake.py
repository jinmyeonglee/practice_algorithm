arr = list(map(int, input().split()))

ans = 0

high = arr[0]
i = 1
while(i < len(arr)):
    if arr[i] <= high:
        high = arr[i]
    else:
        temp = 0
        while(i < len(arr) and high <= arr[i]):
            temp += high - arr[i]
            i += 1
        ans += temp
        if i < len(arr): high = arr[i]
        print(temp)
        print("ans", ans)
    i += 1

print(ans)