import bisect

def find_gt(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_word(words, input) :
    dict = {}
    for i in range(len(input)):
        if input[i] in dict:
            dict[input[i]].append(i)
        else :
            dict[input[i]] = [i]

    ans = "NONE"
    for word in words:
        idx = -1
        flag = 1
        for i in word:
            try:
                if i not in dict:
                    flag = 0
                    break
                idx = find_gt(dict[i], idx)
            except ValueError:
                flag = 0
                break
        if flag == 1:
            ans = word

    return ans

def main():
    words = ["able","apple","kangaroo"]
    input = "abppplle"
    print(find_word(words, input))

if __name__== "__main__":
    main()

