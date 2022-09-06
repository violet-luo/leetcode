def lengthOfLongestSubstring(s):
    arr_len = 0
    l, r = 0, 0
    chars = set()
    
    while r < len(s):
        if s[r] not in chars:
            arr_len = max(arr_len, r - l + 1)
            chars.add(s[r])
            r += 1
        else:
            chars.remove(s[l])
            l += 1
    
    return arr_len
