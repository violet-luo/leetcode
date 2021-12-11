def firstUniqChar(s):
    dic = {}

    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    for i in range(len(s)):
        char = s[i]
        if dic[char] == 1:
            return i
    return -1

"""
1. get
"""
def firstUniqChar(self, str):
    dic = {}

    for char in dic:
        # 当char还不在dic时，dic[char] += 1 is not supported
        dic[char] = dic.get(char, 0) + 1 

    for char in str:
        if dic[char] == 1:
            return char

"""
2. defaultdict
"""

from collections import defaultdict
class Solution:
    def firstUniqChar(self, str):
        dic = defaultdict(int)

        for char in str:
            dic[char] += 1

        for char in str:
            if dic[char] == 1:
                return char
