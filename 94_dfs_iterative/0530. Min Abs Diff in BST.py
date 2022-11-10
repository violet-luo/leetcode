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
