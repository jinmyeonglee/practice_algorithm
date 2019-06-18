def countBits(num):
    if num == 0:
        return [0]
    bits = [0] * (num + 1)
    bits[1] = 1

    b = 2
    while b <= num:
        for i in range(b, b * 2):
            if i <= num:
                bits[i] = bits[i % b] + 1
        b *= 2

    return bits


if __name__ == "__main__":
    num = int(input())
    ans = countBits(num)
    print(ans)

