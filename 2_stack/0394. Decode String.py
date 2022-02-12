def decodeString(s):
    res = []
    for c in s:
        # loop till ']' and add ele to ['3', '[', 'a', '2', '[']
        if c != ']':
            res.append(c)
            continue
        
        # retrieve letters #['c'] #['cc', 'a']
        letters = []
        while res and res[-1] != '[':
            letters.append(res.pop())

        # skip '['
        res.pop()
        
        num = 0
        base = 1
        while res and res[-1].isdigit():
            num += (ord(res.pop()) - ord('0')) * base
            base *= 10
            # 不能这样写，100会变成1
            # cur_num = int(res.pop())
            # num += num*10 + cur_num
        # 因为是stack所以要reverse
        res.append(''.join(reversed(letters)) * num)

    return ''.join(res)
decodeString('3[a2[c]]')
