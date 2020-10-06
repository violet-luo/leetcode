"""

Runtime: 32 ms, faster than 79.53% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.3 MB, less than 5.14% of Python3 online submissions for Longest Common Prefix.

"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 
