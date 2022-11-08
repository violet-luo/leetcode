def decodeString(s):
    stack, res, num = [], "", 0
    for c in s:
        if c == '[': # [[3, ""]]
            stack.append([num, res])
            res, num = "", 0 # 归零
        elif c == ']':
            cur_num, last_res = stack.pop()
            res = last_res + cur_num * res
        elif '0' <= c <= '9':
            num = num * 10 + int(c)            
        else: # char为字母
            res += c
    return res
