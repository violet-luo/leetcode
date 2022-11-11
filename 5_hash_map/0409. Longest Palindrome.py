def longestPalindrome(self, s):
    res = set()

    for c in s:
        if c in res:
            res.remove(c) # 偶数个
        else:
            res.add(c) # 奇数个

    # len(res)存储了所有奇数
    if len(res) > 0: # 偶数个 + 1个奇数
        return len(s) - len(res) + 1
    else: # 无奇数，直接return原string
        return len(s)
