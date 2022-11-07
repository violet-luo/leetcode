def removeDuplicates(self, s, k):
    res = []  # pair of [char, freq]
    for char in s: # [d, 1]
        if res and res[-1][0] == char:
            res[-1][1] += 1
        else:
            res.append([char, 1])
        if res[-1][1] == k:
            res.pop()
    return "".join(char * cnt for char, cnt in res) # ['a', 2]
