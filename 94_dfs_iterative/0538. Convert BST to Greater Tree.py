def convertBST(self, root):
     if not root:
         return 
     
     node, stack, s = root, [], 0
     while node or stack: 
         while node:
             stack.append(node)
             node = node.right
         node = stack.pop()
         if node:
             tmp = s
             s += node.val
         node.val += tmp
         node = node.left

     return root
