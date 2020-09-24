"""

Runtime: 48 ms, faster than 43.34% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14 MB, less than 78.05% of Python3 online submissions for Isomorphic Strings.

"""

def isIsomorphic(self, s: str, t: str) -> bool:
    dic = {}

    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        elif t[i] in dic.values():
            return False
        else:
            dic[s[i]] = t[i]
    return True
