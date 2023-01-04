def mergeTrees(self, root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    queue = collections.deque([(root1,root2)])
    while queue:
        r1,r2 = queue.popleft()
        r1.val += r2.val
        # 如果r1和r2的左子树都不为空，就放到队列中
        # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
        if r1.left and r2.left:
            queue.append((r1.left,r2.left))
        elif not r1.left:
            r1.left = r2.left
        if r1.right and r2.right:
            queue.append((r1.right,r2.right))
        elif not r1.right:
            r1.right = r2.right
    return root1
