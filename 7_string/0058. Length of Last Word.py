"""

Runtime: 24 ms, faster than 94.77% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.1 MB, less than 13.96% of Python3 online submissions for Length of Last Word.

"""

def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])
