"""
1. Two Pointers
"""

def strStr(self, haystack, needle):
    i, j = 0, 0
    h, n = len(haystack), len(needle)

    for i in range(h - n + 1): # 10 - 3 + 1 => [0, 7)
        for j in range(n):
            if haystack[i + j] != needle[j]: # 而不是haystack[i] != needle[j]
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
