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
