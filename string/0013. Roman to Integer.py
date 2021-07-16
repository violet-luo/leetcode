"""
Credit to @wenfengqiu

abc

1. if a < b, then b - a
2. if a > b, then a + b
3. the last digit is always positive

Runtime: 48 ms, faster than 56.62% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.7 MB, less than 5.38% of Python3 online submissions for Roman to Integer.
"""

def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
