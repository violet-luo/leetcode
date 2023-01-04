def widthOfBinaryTree(self, root):
    if not root: 
        return []
    
    res = 0
    queue = collections.deque([(root,1)])

    while queue:
        # Put all children of current level in next_level.
        res = max(res, queue[-1][1] - queue[0][1] + 1)
        level = []
        for node, num in queue:
            if node.left:   # Make sure to not put the Null nodes
                level.append((node.left, num * 2))
            if node.right:
                level.append((node.right, num * 2 + 1))
        queue = level
    return res
