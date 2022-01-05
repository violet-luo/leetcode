def isPalindrome(self, s):
    start, end = 0, len(s) - 1
    while start < end:
        # 每次要判断left < right, 不然会越界
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if start < end and s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True
