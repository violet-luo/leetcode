❌❌❌
def validPalindrome(self, s):
    left, right = 0, len(s) - 1
    
    # 找到第一个不一样的，删除
    while left < right:
        if s[left] != s[right]:
            # 不能这样，'abca'要测试'aba'和'aca'
            s = s[:left] + s[left+1:]             
        else:
            left += 1
            right -= 1

    # 重走一遍，即125.Valid Palindrome
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


✅✅✅
def validPalindrome(self, s):
    left, right = 0, len(s) - 1

    # 找到第一个不一样的，删除
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
    return True # 一定要加这一行，'aba'才是True，不然会return None

def isPalindrome(self, s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
