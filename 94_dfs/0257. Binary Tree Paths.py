def binaryTreePaths(self, root):
    if root is None:
        return []
        
    if root.left is None and root.right is None:
        return [str(root.val)] #递归出口

    leftPaths = self.binaryTreePaths(root.left) #2 #["5"]
    rightPaths = self.binaryTreePaths(root.right) #3 #None
    
    paths = []
    for path in leftPaths + rightPaths:
        paths.append(str(root.val) + '->' + path) #["2->5", "3"]
        
    return paths
