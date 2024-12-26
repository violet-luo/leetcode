def simplifyPath(self, path: str) -> str:
    paths = path.split('/')
    stack = []

    for p in paths:
        if p == '':
            continue
        elif p == '.':
            continue
        elif p == '..':
            if len(stack) > 0:
                stack.pop()
            else:
                continue
        else:
            stack.append(p)
    
    return '/' + '/'.join(stack)
    
###

def simplifyPath(self, path):
    path = path.split('/')
    stack = []
    for i in path:
        # 遇到 ".." 则从栈顶弹出一个元素 (如果栈为空则不弹栈, 对应 "/../")
        if i == '..':
            if len(stack):
                stack.pop()
        # 遇到正常的目录名, 入栈
        elif i != '.' and i != '':
            stack.append(i)
    return '/' + '/'.join(stack)
