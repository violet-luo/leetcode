def averageOfLevels(self, root):
    if not root:
        return []

    queue = collections.deque([root])
    res = []

    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(sum(level)/len(level))
    return res
