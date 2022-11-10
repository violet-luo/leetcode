def getLonelyNodes(self, root):
    res, stack = [], [root]

    while stack: 
        node = stack.pop()
        if node.left: 
            stack.append(node.left)
            if not node.right: 
                res.append(node.left.val)
        if node.right: 
            stack.append(node.right)
            if not node.left: 
                res.append(node.right.val)
    return res 
