def calculate(self, s):
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            res += sign * num
            num = 0 
            sign = 1 
        elif c == '-':
            res += sign * num
            num = 0 
            sign = -1 
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif c == ')':
            res += sign * num
            num = 0 
            res *= stack[-1]
            res += stack[-2]
            stack = stack[:-2]
    res += sign * num
    return res
