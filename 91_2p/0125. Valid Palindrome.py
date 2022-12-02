def isPalindrome(self, s: str) -> bool:
    s = ''.join(ch for ch in s if ch.isalnum())
    s = s.lower()
    
    left, right = 0, len(s) - 1
    
    while left < right: # <= 也可
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    
    return True

##

def isPalindrome(self, s):
    l, r = 0, len(s) - 1
    while l < r:
        # 每次要判断left < right, 不然会越界
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
