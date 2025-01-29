def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0
    q = collections.deque([(root, 0)])

    while q:
        node, total = q.pop()
        total = total * 2 + node.val
        if not node.left and not node.right:
            res += total
        if node.left:
            q.append((node.left, total))
        if node.right:
            q.append((node.right, total))
    
    return res
  
###

def sumRootToLeaf(self, root, val): 
    stack = [[root, ""]]
    result = 0
 
    while stack:
        current, path = stack.pop()
        
        if current.left:
            stack.append([current.left, path+str(current.val)])
        if current.right:
            stack.append([current.right, path+str(current.val)])
        
        if not current.left and not current.right:
            path += str(current.val)
            result += int(path, 2)
            
    return result
