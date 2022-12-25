from collections import Counter
def lengthOfLongestSubstringTwoDistinct(s):
    max_len, counter = 0, Counter()
    n = len(s)
    left = 0

    for right in range(n):
        counter[s[right]] += 1
        while right < n and len(counter) > 2:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
        
    return max_len
