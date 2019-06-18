import collections
str1 = "ZAZAZA"
str2 = "ABZ"


def minConcat(a, b):
    res = 0
    d = {}
    for i in range(len(str2)):
        d[str2[i]] = i

    pre = float('-inf')

    for i in range(len(str1)):
        if d[str1[i]] < pre:
            for key in d.keys():
                d[key] += len(str2)
            print(d)
            res += 1
        pre = d[str1[i]]
    print(d)
    return res


if __name__ == "__main__":
    print(minConcat(str1, str2))
