def inorderTraversal(self, root):
    if not root:
        return []
    
    res, stack = [], []
    
    while root:
        stack.append(root)
        root = root.left
    
    while stack:
        node = stack.pop()
        res.append(node.val) # 左叶子1, 2, 3
        
        if node.right: # 4
            node = node.right 
            while node: 
                stack.append(node)
                node = node.left
    
    return res
