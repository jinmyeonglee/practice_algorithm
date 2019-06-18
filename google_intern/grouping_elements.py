arr_1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
arr_1 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]  # False
arr_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]  # True
arr_1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


# for sorted, duplicated.
def isGrouping2(arr):
    check = [False] * len(arr)

    for _ in range(len(arr) // 5):
        base = None
        for j in range(len(check)):
            if not check[j]:
                base = arr[j]
                check[j] = True
                break
        for i in range(len(arr)):
            if not check[i] and base + 1 <= arr[i] <= base + 4:
                check[i] = True

    for k in check:
        if not k:
            print(check)
            return False
    return True


# if arr is sorted array:
def isGrouping(arr):
    for i in range(len(arr) // 5):
        check = arr[i * 5 + 4]
        for j in range(4):
            if arr[i * 5 + j] + (4 - j) != check:
                return False

    return True


if __name__ == "__main__":
    print(isGrouping2(arr_1))
