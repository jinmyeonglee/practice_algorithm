arr1 = [1, 3, 4, 6, 10, 9, 8, 7, 4, 2]
arr1 = [1, 2, 3, 4, 5, 6, 9, 10, 4, 2]
arr1 = [1, 2, 2, 2, 3, 10, 10, 9, 8, 7, 6, 4, 3, 2]

def updown_max(arr):
    cur = len(arr) // 2
    pre = 0

    if len(arr) == 1:
        return arr[0]

    while 0 < cur < len(arr) - 1 \
            and not (arr[cur - 1] <= arr[cur] and arr[cur + 1] <= arr[cur]):
        if arr[cur - 1] <= arr[cur] <= arr[cur + 1]:
            cur = (len(arr) - cur) // 2 + cur
        else:
            cur = (cur + pre) // 2
            pre = cur

    return arr[cur]


if __name__ == "__main__":
    k = updown_max(arr1)
    print(k)
