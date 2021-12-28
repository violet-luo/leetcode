def firstUniqChar(self, s):
    dic = {}

    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    index = 0
    for char in s:
        if dic[char] == 1:
            return index
        index += 1
    return -1

def firstUniqChar(self, s):
    count = collections.Counter(s)

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1
