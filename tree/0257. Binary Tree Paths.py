"""

Runtime: 28 ms, faster than 92.64% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.8 MB, less than 61.88% of Python3 online submissions for Binary Tree Paths.

"""

def binaryTreePaths(self, root):
    if root is None:
        return []
        
    if root.left is None and root.right is None:
        return[str(root.val)]
    
    leftPaths = self.binaryTreePaths(root.left)
    rightPaths = self.binaryTreePaths(root.right)
    
    paths = []
    for path in leftPaths + rightPaths:
        paths.append(str(root.val) + '->' + path)
        
    return paths
