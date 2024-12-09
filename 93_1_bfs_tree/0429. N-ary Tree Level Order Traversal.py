def levelOrder(self, root: 'Node') -> List[List[int]]:
   if not root:
       return []
       
   q = collections.deque([root])
   res = []

   while q:
       level = []
       for i in range(len(q)):
           node = q.popleft()
           level.append(node.val)
           for child in node.children:
               q.append(child)
       res.append(level)
   return res
