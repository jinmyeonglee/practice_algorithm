from collections import OrderedDict
N = int(input())

words = []

for _ in range(N):
    word = input()
    words.append(word)

words.sort()
words.sort(key=lambda k: len(k))

res = OrderedDict()
for word in words:
    if word not in res:
        res[word] = ""
words = res.keys()
for word in words:
    print(word)
