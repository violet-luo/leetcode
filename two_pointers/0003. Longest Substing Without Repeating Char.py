"""

1. Hash Map
Runtime: 48 ms, faster than 94.48% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 73.40% of Python3 online submissions for Longest Substring Without Repeating Characters.

"""
def lengthOfLongestSubstring(self, s: str) -> int:
    k, res, c_dict = -1, 0, {}
    for i, c in enumerate(s):
        if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
            k = c_dict[c]
            c_dict[c] = i
        else:
            c_dict[c] = i
            res = max(res, i-k)
    return res
    
"""
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    longest = 0
    left, right = 0, 0
    chars = set()
    while right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            longest = max(longest, right - left)
        else:
            chars.remove(s[left])
            left += 1
    return longest
