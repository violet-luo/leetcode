def longestPalindrome(self, s):
    dic = {}

    for char in s:
        if char in dic:
            del dic[char] # 偶数个
        else:
            dic[char] = 1 # 奇数个

    if len(dic) > 0:
    # 偶数个 + 1个奇数
        return len(s) - len(dic) + 1
    else:
        # 无奇数，直接return原string
        return len(s)
      
def longestPalindrome(self, s):
    hash = set()

    for c in s:
        if c in hash:
            hash.remove(c) # 偶数个
        else:
            hash.add(c) # 奇数个

    # len(hash)存储了所有奇数
    if len(hash) > 0:
        # 偶数个 + 1个奇数
        return len(s) - len(hash) + 1
    else:
        # 无奇数，直接return原string
        return len(s)
