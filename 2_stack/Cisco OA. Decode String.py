def decodeString(s):
    stack = []
    letter = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num*10 + int(ch)
        elif ch.isalpha():
            letter += ch
        elif ch == "(": #存储（）中的字母
            stack.append(letter)
            letter = ""
        elif ch == "}": 
            prev_res = stack.pop() # 'ab'
            letter = pre_res + letter * num # 'ab' + 'ddd' 
            num = 0
    
    while stack:
        letter = stack.pop() + letter
    return letter
