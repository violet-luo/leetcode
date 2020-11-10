"""

1. Two Pointers
Runtime: 32 ms, faster than 63.09% of Python3 online submissions for Implement strStr().
Memory Usage: 14.2 MB, less than 8.23% of Python3 online submissions for Implement strStr().

"""

def strStr(self, haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)

    if needle == "":
        return 0

    for i in range(m - n + 1):
        for j in range(n):
            if haystack[i+j] != needle[j]:
                break
            if j == n - 1:
                return i
    return -1
   
   
"""
"""
def strStr(self, haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
