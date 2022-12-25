from collections import Counter
def kDistinctCharacters(s, k):
    max_len, counter = 0, Counter()
    n = len(s)
    left = 0

    for right in range(n):
        counter[s[right]] += 1
        while left < n and len(counter) >= k:
            # 每次挪动l都需要加上 n - right
            max_len += n - right
            counter[s[left]] -= 1 
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1        
    return max_len
