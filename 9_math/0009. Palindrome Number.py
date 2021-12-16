/*

1. Convert to str

Runtime: 52 ms, faster than 94.03% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 9.81% of Python3 online submissions for Palindrome Number.

*/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        s = str(x)
        
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                return False
        return True
        
        
/*

2. Reverse the number

Runtime: 60 ms, faster than 81.20% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 57.47% of Python3 online submissions for Palindrome Number.

*/

def isPalindrome(self, x: int) -> bool:
	if x < 0:
        return False
    a, b = x, 0
    while x:
        b *= 10
        b += x % 10
        x //= 10
    return a == b
