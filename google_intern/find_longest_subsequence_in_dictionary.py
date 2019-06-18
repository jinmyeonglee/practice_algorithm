import bisect
import collections


def find_gt(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError



def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)

    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)

    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                break
            pos = possible_positions[0] + 1
        else:
            return word


def find_longest_sub(S, D):
    words = sorted(D, key=lambda w: len(w), reverse=True)  # WlogW
    pos = {}
    for index, c in enumerate(S):  # N
        if c in pos:
            pos[c].append(index)
        else:
            pos[c] = [index]

    for word in words:  # W
        loc = -1
        for c in word:  # P
            if c in pos:
                try:
                    temp = find_gt(pos[c], loc)
                except ValueError:
                    break
                if temp > loc:
                    loc = temp
                else:
                    break
            else:
                break
        else:
            return word
    print(pos)


if __name__ == "__main__":
    D = {"able", "ale", "apple", "bale", "kangaroo"}
    S = "kanaarrgadsordsoo"
    re = find_longest_sub(S, D)
    print(re)
    S = "aefefpfbescpppfgflle"
    re = find_longest_sub(S, D)
    print(re)
    S = "ppppaaaaefdsfeflselllleee"
    re = find_longest_sub(S, D)
    print(re)