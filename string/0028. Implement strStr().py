"""

Runtime: 20 ms, faster than 98.98% of Python3 online submissions for Implement strStr().
Memory Usage: 14.2 MB, less than 21.47% of Python3 online submissions for Implement strStr().

"""

def strStr(self, haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
