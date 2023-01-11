def mergeTrees(self, root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    queue = collections.deque([(root1,root2)])
    while queue:
        l, r = queue.popleft()
        l.val += r.val
        
        # 顺序可变    
        if l.left and r.left: # 如果l和r的左子树都不为空，就放到队列中
            queue.append((l.left, r.left))
        if l.right and r.right:
            queue.append((l.right, r.right))
        if not l.left: # 如果l的左子树为空，就把r的左子树挂到l的左子树上
            l.left = r.left
        if not l.right:
            l.right = r.right
    return root1
