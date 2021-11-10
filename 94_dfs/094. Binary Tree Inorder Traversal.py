//1. DFS
def preorderTraversal(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

//2. BFS
def inorderTraversal(self, root):
   if not root:
       return []
       
   res, stack = [], []

    while stack or root:
        if root:# 走到左子树最底层
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right   
    return res
