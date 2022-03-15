# 1.
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

# 2.
def binaryTreePaths(self, root): #1 #2 #5
    if root.left is None and root.right is None:
        return [[root.val]] #[[5]]
    paths = []

    if root.left:
        leftPaths = self.binaryTreePaths(root.left) #get(2) #get(5)
        leftPaths = [[root.val] + p for p in leftPaths] # [[5,2]]
        paths += leftPaths #[[5,2]]

    if root.right:
        rightPaths = self.binaryTreePaths(root.right) 
        righPaths = [[root.val] + p for p in rightPaths]
        paths += righPaths

    return paths
