def findBottomLeftValue(self, root):
    if not root:
        return []

    queue = collections.deque([root])
    res = []

    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.right: #因为要return left most, 先attach右子树
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        res.append(level)
    return res[-1].pop() #最后是list of list, res[-1] = [[1,3]], 所以要加pop()
