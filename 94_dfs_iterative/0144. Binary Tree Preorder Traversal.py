def preorderTraversal(self, root):
     res, stack = [], []
     node = root 
     while node or stack:
         while node:
             res.append(node.val)
             stack.append(node)
             node = node.left
         node = stack.pop()
         node = node.right
     
     return res
