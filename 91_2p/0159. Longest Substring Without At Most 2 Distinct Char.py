def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    l, arr_len = 0, 0
    counter = {}

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1
        if len(counter) > 2:
            counter[s[l]] -= 1
            if counter[s[l]] == 0:
                del counter[s[l]]
            l += 1
        arr_len = max(arr_len, r - l + 1)

    return arr_len
