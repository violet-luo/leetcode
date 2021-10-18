def levelOrderBottom(self, root):
    import collections
    ans = []  
    if root is None:  
        return ans  
    q = collections.deque()
    q.append(root)  
    #层次遍历
    while len(q) is not 0:  
        row = []  
        for i in range(len(q)):  
            if q[0].left:  #左子树不为空的话压入队列
                q.append(q[0].left)  
            if q[0].right:   #右子树不为空的话压入队列
                q.append(q[0].right)  
            row.append(q[0].val)
            q.popleft()
        ans += [row]  #储存当前层的节点
    #倒序 
    ans = ans[::-1]
    return ans
