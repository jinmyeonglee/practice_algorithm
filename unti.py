import pprint
n = int(input())
M = []

for i in range(n):
    M.append(list(map(int, input().strip().split())))
pp = pprint.PrettyPrinter(width=20, indent=4)

pp.pprint(M)
