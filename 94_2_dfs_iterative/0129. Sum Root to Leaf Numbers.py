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
