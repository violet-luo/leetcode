def removeInvalidParentheses(self, s): #'(a()'
    if not s:
        return ['']
    queue = collections.deque([s])
    res, visited = [], set([s])
    found = False
    
    while queue:
        cur = queue.popleft()
        if self.is_valid(cur): # 递归出口，找删除最小的有效字符串
            found = True # 找到最小的就不用再删除了
            res.append(cur)
        elif not found:
            # 穷尽S去掉range(0, n)个括号的变种
            for i in range(len(cur)):
                if cur[i] == '(' or cur[i] == ')':
                    t = cur[:i] + cur[i + 1:] # 'a()','(a)', '(a('
                    if t not in visited:
                        queue.append(t)
                        visited.add(t)
    return res
    
def is_valid(self, s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1 
        elif c == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0
