def removeDuplicates(self, s, k):
    res = []  # pair of [char, freq]
    for char in s: 
        if res and res[-1][0] == char: # [['d',1], ['e',3]]
            res[-1][1] += 1
        else:
            res.append([char, 1]) # [['d',1]]
        if res[-1][1] == k: # ['e',3]
            res.pop()
    return "".join(char * cnt for char, cnt in res) # ['a', 2]
