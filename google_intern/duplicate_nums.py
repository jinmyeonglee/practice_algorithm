a = [1, 3, 5]
b = [1, 2, 2, 3, 3, 5, 5, 10, 11]
elements = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] == b[j] and (len(elements) == 0 or elements[-1] != a[i]):
        elements.append(a[i])
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(elements)

