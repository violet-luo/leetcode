def lengthOfLongestSubstring(self, s: str) -> int:
    max_len = 0
    l = 0
    seen = set()

    for r in range(len(s)):
        while s[r] in seen: # Remove characters until the duplicate is gone
            seen.remove(s[l])
            l += 1
        
        max_len = max(max_len, r - l + 1)
        seen.add(s[r])
    
    return max_len
