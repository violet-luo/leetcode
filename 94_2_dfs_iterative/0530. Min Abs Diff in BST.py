def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    min_val = float('inf')
    stack, res = [], []

    while root:
        stack.append(root)
        root = root.left
    
    while stack:
        node = stack.pop()
        if res: # 与中序遍历唯一不同
            min_val = min(min_val, abs(node.val - res[-1]))
        res.append(node.val)
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
    
    return min_val
   
###

def getMinimumDifference(self, root):
   stack = []
   node = root
   pre = None
   res = float('inf')
   while node or stack:
      while node:
         stack.append(node)
         node = node.left
      node = stack.pop()
      if pre:
         res = min(res, abs(node.val - pre.val))
      pre = node
      node = node.right
   return res
