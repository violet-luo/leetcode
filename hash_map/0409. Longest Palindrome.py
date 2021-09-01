def longestPalindrome(self, s):
    hash = set()

    for c in s:
        if c not in hash:
            # 奇数个
            hash.add(c)
        else:
            # 偶数个
            hash.remove(c)

    # len(hash)存储了所有奇数
    if len(hash) > 0:
        # 偶数个 + 1个奇数
        return len(s) - len(hash) + 1
    else:
        # 无奇数，直接return原string
        return len(s)
