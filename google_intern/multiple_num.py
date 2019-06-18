def multiple_num(num):
    re = 1
    while num >= 10:
        re *= num % 10
        num //= 10
    re *= num
    return re


def invalid(num):
    arr = [0] * 8
    for i in range(2, 10):
        while num % i == 0:
            arr[i - 2] += 1
            num //= i
    if num < 10:
        return False, arr
    else:
        return True, arr


def main():
    N = int(input())

    isinvalid, arr = invalid(N)
    if isinvalid:
        return -1

    if N < 10:
        return N
    res = []
    for i in range(8):
        k = 1
        while arr[i] > 0:
            k *= (i + 2)
            if k > 10:
                k //= (i + 2)
                res.append(k)
                k = 1
            else:
                arr[i] -= 1
        if k != 1:
            res.append(k)

    res.sort(reverse=True)

    answer = 0
    base = 1
    for i in res:
        answer += base * i
        base *= 10

    return answer


if __name__ == "__main__":
    a = main()
    print(a)
