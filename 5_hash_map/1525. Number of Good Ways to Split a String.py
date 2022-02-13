import collections
def numSplits(s):
    left = collections.Counter()
    right = collections.Counter(s) #{'a':4，'c':1, 'b':1}
    res = 0
    
    for c in s:
        left[c] += 1
        right[c] -= 1
        if right[c] == 0:
            del right[c]
            
        # 左右拥有相同的独特字符数
        if len(left) == len(right):
            res += 1

    return res
