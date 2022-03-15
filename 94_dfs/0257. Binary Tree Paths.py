def binaryTreePaths(self, root):
    paths = []
    if not root:
        return paths
    if not root.left and not root.right: #递归出口
        return[str(root.val)]
    
    leftPaths = self.binaryTreePaths(root.left) #2 #["5"]
    rightPaths = self.binaryTreePaths(root.right) #3 #None
    
    paths = []
    for path in leftPaths + rightPaths:
         paths.append(str(root.val) + '->' + path) #["2->5", "3"]
        
    return path
