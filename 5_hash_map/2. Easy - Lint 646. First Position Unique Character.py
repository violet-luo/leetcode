def firstUniqChar(self, s):
    alp = {}
    for c in s:
        if c not in alp:
            alp[c] = 1
        else:
            alp[c] += 1

    index = 0
    for c in s:
        if alp[c] == 1:
            return index
        index += 1 # cannot omit
    return -1
