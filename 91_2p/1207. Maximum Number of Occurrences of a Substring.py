def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    substring_count = defaultdict(int)
    char_to_freq = defaultdict(int)
    l = 0
    
    for r in range(len(s)):
        char_to_freq[s[r]] += 1

        if r - l + 1 > minSize:
            char_to_freq[s[l]] -= 1
            if char_to_freq[s[l]] == 0:
                del char_to_freq[s[l]]
            l += 1

        if r - l + 1 == minSize and len(char_to_freq) <= maxLetters:
            substring_count[s[l:r+1]] += 1

    return max(substring_count.values(), default=0)
