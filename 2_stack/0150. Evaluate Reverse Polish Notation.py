def evalRPN(self, tokens):
    stack = []

    for t in tokens:
        if t not in ["+", "-", "*", "/"]:
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop()
            if t == "+": stack.append(a + b)
            elif t == "-": stack.append(a - b)
            elif t == "*": stack.append(a * b)
            else: stack.append(int(a / b))
    return stack.pop()
