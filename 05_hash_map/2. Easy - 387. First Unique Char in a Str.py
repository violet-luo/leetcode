"""
1. Return the char
"""
def firstUniqChar(self, str):
    counter = {}

    for c in str:
        counter[c] = counter.get(c, 0) + 1

    for c in str:
        if counter[c] == 1:
            return c

"""
2. Return the index
"""
def firstUniqChar(self, str):
    count = collections.Counter(s)

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1
