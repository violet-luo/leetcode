def decodeString(s):
    stack, res, num = [], "", 0
    for ch in s:
        if ch == '[': # [[3, ""]]
            stack.append([num, res])
            res, num = "", 0 # 归零
        elif ch == ']':
            cur_num, last_res = stack.pop()
            res = last_res + cur_num * res
        elif ch.isdigit():
            num = num * 10 + int(ch)            
        else: # char为字母
            res += ch
    return res
