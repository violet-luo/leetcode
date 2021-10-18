def zigzagLevelOrder(self, root):
    import collections
    # write your code here
    if root is None:
        return []
    ans = []
    q = collections.deque()
    q.append(root)
    #正反向标志
    isForward = 1
    while len(q) is not 0:
        row = []
        for i in range(len(q)):
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            row.append(q[0].val)
            q.popleft()
        #根据标志来确认当前层遍历的方向
        row = row[::isForward]#翻转
        ans += [row]
        #方向反转
        isForward *= -1
    return ans
