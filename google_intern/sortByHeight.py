k = [(177, 0), (180, 0), (168, 0), (158, 2), (170, 1)]


def sortByNum(arr):
    res = [None for _ in range(len(arr))]
    arr.sort(key=lambda x: x[0])

    for h, n in arr:
        count = 0
        for r in range(len(res)):
            if res[r] is None:
                if n == count:
                    res[r] = h
                    break
                else:
                    count += 1
    return res


if __name__ == "__main__":
    b = sortByNum(k)
    print(b)
