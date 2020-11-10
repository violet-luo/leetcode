"""

Runtime: 40 ms, faster than 89.10% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.4 MB, less than 10.54% of Python3 online submissions for Valid Palindrome.

"""

def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True
