def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    l = 0
    max_len = 0
    char_to_freq = collections.defaultdict(int)

    for r in range(len(s)):
        char_to_freq[s[r]] += 1
        while len(char_to_freq) > k:
            char_to_freq[s[l]] -= 1
            if char_to_freq[s[l]] == 0:
                del char_to_freq[s[l]]
            l += 1
        max_len = max(max_len, r - l + 1)
        
    return max_len
