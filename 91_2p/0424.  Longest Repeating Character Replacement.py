from collections import Counter
def characterReplacement(s, k):
    max_len, counter, res = 0, Counter(), 0
    left = 0
    
    for right in range(len(s)):
        counter[s[right]] += 1
        max_len = max(max_len, counter[s[right]])
        # 如果要替换的次数超过k, 移动左边界，直到不超出
        while right - left + 1 - max_len > k:
            counter[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    
    return res
