def lengthOfLongestSubstring(s):
    max_len, seen = 0, set()
    n = len(s)
    right = 0

    for left in range(n):
        while right < n and s[right] not in seen:
            seen.add(s[right])
            right += 1
        # 走到第一个重复
        max_len = max(max_len, right - left)
        seen.remove(s[left])
    
    return max_len
