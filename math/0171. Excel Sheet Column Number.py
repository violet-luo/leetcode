"""

Runtime: 32 ms, faster than 61.28% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.1 MB, less than 99.95% of Python3 online submissions for Excel Sheet Column Number.

"""
def titleToNumber(self, s: str) -> int:
    res = 0
    for i in s:
        res = res*26 + ord(i)-ord('A')+1 # ord returns unicode
    return res
