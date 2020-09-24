"""

Runtime: 28 ms, faster than 72.65% of Python3 online submissions for Word Pattern.
Memory Usage: 13.6 MB, less than 97.17% of Python3 online submissions for Word Pattern.

"""

def wordPattern(self, pattern: str, s: str) -> bool:
    dic = {}

    s = s.split()

    if len(pattern) != len(s):
        return False

    for i in range(len(pattern)):
        if pattern[i] not in dic:
            # pattern = "abba" s = "dog dog dog dog"
            if s[i] in dic.values():
                return False
            dic[pattern[i]] = s[i]
        else:
            if dic[pattern[i]] != s[i]:
                return False
    return True
