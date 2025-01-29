def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = 0
    q = collections.deque([(root, 0)])

    while q:
        node, total = q.pop()
        total = total * 10 + node.val
        if not node.left and not node.right:
            res += total
        if node.left:
            q.append((node.left, total))
        if node.right:
            q.append((node.right, total))
    
    return res

###

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    paths = []

    q = [(root, str(root.val))]
    while q:
        cur, path = q.pop()
        if not cur.left and not cur.right:
            paths.append(path)
        if cur.left:
            q.append([cur.left, path + str(cur.left.val)])
        if cur.right:
            q.append([cur.right, path + str(cur.right.val)])
    
    res = 0
    for p in paths:
        res += int(p)
    
    return res

###

def sumNumbers(self, root):
    stack = [[root, ""]]
    result = 0
    
    # Traverse nodes by stacking them
    while stack:
        current, path = stack.pop()
        
        if current.left:
            stack.append([current.left, path+str(current.val)])
        if current.right:
            stack.append([current.right, path+str(current.val)])
        
        if not current.left and not current.right:
            path += str(current.val)
            result += int(path, 10)
            
    return result
