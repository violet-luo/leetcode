def canPermutePalindrome(self, s):
    res = set()

    for char in s:
        if char in res:
            res.remove(char) # 偶数个
        else:
            res.add(char) # 奇数个

    # 偶数个 + 1个奇数
    if len(res) > 1:
        return False
    return True
