S = input()

size = len(S)
length_arr = []
i = 0

while i < size:
    chars = {}
    chars[S[i]] = ""
    for j in range(i + 1, size):
        if S[j] not in chars:
            chars[S[j]] = ""
            if len(chars) >= 3:
                length_arr.append(j - i)
                i = j - 2
                break
    else:
        if len(chars) <= 2:
            length_arr.append(j - i + 1)
    i += 1

print(max(length_arr))
