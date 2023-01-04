def preorderTraversal(self, root):
    if not root:
       return []
       
    res, stack = [], [root]
    
    while stack:
       node = stack.pop()
       res.append(node.val)
       if node.right: #先存入右子树，因为之后要先pop左子树
           stack.append(node.right)
       if node.left:
           stack.append(node.left)

    return res 
