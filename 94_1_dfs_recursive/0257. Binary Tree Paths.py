def binaryTreePaths(self, root):
    def construct_paths(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:  # 当前节点是叶子节点
                paths.append(path) 
            else:
                path += '->'  # 当前节点不是叶子节点，继续递归遍历
                construct_paths(root.left, path)
                construct_paths(root.right, path)

    paths = []
    construct_paths(root, '')
    return paths

###

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

###

def binaryTreePaths(self, root):
    if not root:
        return []
        
    res = []
    self.dfs(root, [str(root.val)], res)
    return res

def dfs(self, node, path, res):
    if not node.left and not node.right:
        res.append('->'.join(path))
        return

    if node.left:
        path.append(str(node.left.val))
        self.dfs(node.left, path, res)
        path.pop()
    
    if node.right:
        path.append(str(node.right.val))
        self.dfs(node.right, path, res)
        path.pop()
