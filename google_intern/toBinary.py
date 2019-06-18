n = int(input())


def decToBinary(num):
    ans = ""
    d = 2
    if num == 0:
        return "0"
    while num > 1:
        if num % 2 == 1:
            ans = "1" + ans
        else:
            ans = "0" + ans
        num //= 2
        d *= 2
    if num == 1:
        ans = "1" + ans
    return ans


if __name__ == "__main__":
    a = decToBinary(n)
    print(a)

