def isValidSerialization(self, preorder):
    stack = []
    for node in preorder.split(','):
        stack.append(node)
        while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
            stack.pop(), stack.pop(), stack.pop()
            stack.append('#')
    return stack == ['#']
