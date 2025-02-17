def checkValidString(self, s: str) -> bool:
    left_stack, asterick_stack = [], []
    n = len(s)

    for i in range(n):
        c = s[i]
        if c == '(':
            left_stack.append(i) # store index, not c
        elif c == '*':
            asterick_stack.append(i)
        else:
            if left_stack:
                left_stack.pop()
            elif asterick_stack:
                asterick_stack.pop()
            else:
                return False
    
    while left_stack and asterick_stack:
        left_index = left_stack.pop()
        asterick_index = asterick_stack.pop()
        if left_index > asterick_index:
            return False
    
    return not left_stack
