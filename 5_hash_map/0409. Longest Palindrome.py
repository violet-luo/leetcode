def longestPalindrome(self, s: str) -> int:
    counter = collections.Counter(s)
    length = 0

    for num, cnt in counter.items():
        if cnt % 2 == 0:
            length += cnt
        elif cnt > 2: # 'ccc'
            length += cnt - 1

    return length + 1 if length < len(s) else length
    
###

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
