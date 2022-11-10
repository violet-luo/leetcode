def postorderTraversal(self, root):
   if not root:
      return []
     
   stack, res = [root], []

   while stack:
      node = stack[-1] # 不能用pop()或是peak()替换
      if not node.left and not node.right:
         stack.pop()
         res.append(node.val)

      if node.right:
          stack.append(node.right)
          node.right = None
      
      if node.left:
          stack.append(node.left)
          node.left = None
          
  return res
