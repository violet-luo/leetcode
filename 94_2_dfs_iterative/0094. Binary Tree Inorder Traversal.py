def inorderTraversal(self, root):
    if not root:
        return []
    
    res = []
    stack = []
    
    # 1. 添加所有最左边节点到栈
    while root:
        stack.append(root)
        root = root.left
    
    while stack:
        # 2. 将左节点加入res
        node = stack.pop()
        res.append(node.val)
        # 3. 如果有右节点，加入stack
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
    
    return res
   
###

def inorderTraversal(self, root):
   res, stack = [], []
   node = root
   while node or stack:
      while node:
          stack.append(node)
          node = node.left
      node = stack.pop()
      res.append(node.val)
      node = node.right
     
   return res
