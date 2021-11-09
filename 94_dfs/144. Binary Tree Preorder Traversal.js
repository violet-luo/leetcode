// 1. DFS
def preorderTraversal(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

// 2. BFS
def preorderTraversal(self, root):
    if not root:
       return []
       
    res = []
    stack = [root] #[1]
    
    while stack:
       node = stack.pop()
       res.append(node.val)
       if node.right: #先存入右子树，因为之后要先pop左子树
           stack.append(node.right)
       if node.left:
           stack.append(node.left)

    return res
