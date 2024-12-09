def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    res = []
    q = collections.deque()
    q.append(root)
    direction = -1

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        direction *= -1
        res.append(level[::direction])
    return res

###

def zigzagLevelOrder(self, root):
    if not root:
       return []
    
    q = collections.deque([root])
    res = []
 
    #正反向标志
    isForward = 1
    
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        #根据标志来确认当前层遍历的方向
        level = level[::isForward] #翻转
        res.append(level)
        #方向反转
        isForward *= -1
    return res
