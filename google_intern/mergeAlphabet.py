s = "ABCcbaccc"
b = "BAaCBbDdcbccc"
b = "ABCcbBbaccCc"


def cutStr(s1):
    ans = ""
    gap = ord('a') - ord('A')
    i = 0
    while i < len(s1):
        if i < len(s1) - 1 and (ord(s1[i]) - ord(s1[i + 1]) == gap
                               or ord(s1[i]) - ord(s1[i + 1]) == -1 * gap):
            i += 1
            pass
        else:
            ans += s1[i]
        i += 1
    return ans


def mergeStrUtil(s1, i, j, check):
    gap = ord('a') - ord('A')

    while i >= 0 and j < len(s1):
        print(i, j, check)
        if check[i]:
            i -= 1
            continue
        if i < len(s1) - 1 and (ord(s1[i]) - ord(s1[i + 1]) == gap
                                or ord(s1[i]) - ord(s1[i + 1]) == -1 * gap):
            check[i] = check[i + 1] = True
            i -= 2
            continue
        if check[j]:
            j += 1
            continue
        if j < len(s1) - 1 and (ord(s1[j]) - ord(s1[j + 1]) == gap
                                or ord(s1[j]) - ord(s1[j + 1]) == -1 * gap):
            check[j] = check[j + 1] = True
            j += 2
            continue
        if ord(s1[i]) - ord(s1[j]) == gap or ord(s1[i]) - ord(s1[j]) == gap * -1:
            check[i] = check[j] = True
            i -= 1
            j += 1
        else:
            break
    print("end")


def mergeStr(s1):
    check = [False for _ in range(len(s1))]
    gap = ord('a') - ord('A')
    i = 0
    while i < len(s1):
        if not check[i] and i < len(s1) - 1 and \
                (ord(s1[i]) - ord(s1[i + 1]) == gap or ord(s1[i]) - ord(s1[i + 1]) == -1 * gap):
            check[i] = check[i + 1] = True
            mergeStrUtil(s1, i - 1, i + 2,  check)
            i += 2
        else:
            i += 1

    ans = ""
    for i in range(len(s1)):
        if not check[i]:
            ans += s1[i]
    return ans


if __name__ == "__main__":
    res = mergeStr(b)
    print(res)
