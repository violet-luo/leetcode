def validPalindrome(self, s):
    l, r = 0, len(s) - 1 # -1 所以s[r]不越界

    while l < r:
        if s[l] == s[r]:
            l += 1 
            r -= 1 
        else:
            # 碰到第一对不符合，删除左边或右边的字符
            return self.helper(s, l, r - 1) or self.helper(s, l + 1, r)
    return True          
            
def helper(self, s, l, r):
    while l < r:
        # 碰到第二对不符合，直接return False
        if s[l] != s[r]:
            return False
        l += 1 
        r -= 1
    return True
