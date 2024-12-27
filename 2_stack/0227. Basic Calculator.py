def calculate(self, s: str) -> int:
    s = s.strip() + '+'  # Add a dummy '+' to process the last number
    stack = []
    num = 0
    sign = '+'
    
    for char in s:
        if char.isdigit():
            num = 10 * num + int(char)
        elif char.isspace():
            continue
        else:
            if sign == '+': 
                stack.append(num)
            elif sign == '-': 
                stack.append(-num)
            elif sign == '*': 
                stack.append(stack.pop() * num)
            elif sign == '/': 
                stack.append(int(stack.pop() / num))
            
            sign = char
            num = 0
    
    return sum(stack)

###

def calculate(self, s):
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(s): # 0, '3'
        if char.isdigit():
            num = 10 * num + int(char)
        if (not char.isdigit() and not char.isspace()) or i == len(s) - 1:
            if sign == '+': stack.append(num)
            elif sign == '-': stack.append(-num)
            elif sign == '*': stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            sign = char
            num = 0
    
    return sum(stack) # [3, 4]
