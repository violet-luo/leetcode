def maxLengthBetweenEqualCharacters(s):
    dict = {} # 存储第一次出现字母的index
    res = -1
    for i, c in enumerate(s): # 0, 'c'
        if c in dict: 
            res = max(res, i - dict[c] - 1)
        else:
            dict[c] = i
    return res
  
# Google OA
def maxLengthBetweenEqualCharacters(s):
    dict = {} # 存储第一次出现字母的index
    max_len = 0
    max_index = 0
    for i, c in enumerate(s): # 0, 'c'
        if c in dict: 
            if (i - dict[c] + 1) > max_len:
                max_len = (i - dict[c] + 1)
                max_index = i
        else:
            dict[c] = i
    return s[dict[s[max_index]] : max_index + 1] 
