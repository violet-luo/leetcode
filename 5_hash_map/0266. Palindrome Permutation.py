def canPermutePalindrome(self, s):
    counter = collections.Counter(s) 
    odd_times_ch = 0
    
    for num, cnt in counter.items():
        if cnt % 2 == 1:
            odd_times_ch += 1
    
    return odd_times_ch <= 1

###

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
