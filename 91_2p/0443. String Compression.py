def compress(self, chars: List[str]) -> int:
    l = 0
    r = 1
    res = 0  # the idx to start writing

    while r <= len(chars):  # r <= len(chars) to handle the last character correctly
        cur_cnt = 1
        while r < len(chars) and chars[r] == chars[r - 1]: # get cnt of the cur char
            cur_cnt += 1
            r += 1

        chars[res] = chars[l] # Write the character to res, i.e. ['a']
        res += 1
        
        if cur_cnt > 1: # Write the count to res, i.e. ['a', '2']
            for digit in str(cur_cnt):
                chars[res] = digit
                res += 1

        l = r
        r = l + 1

    return res
