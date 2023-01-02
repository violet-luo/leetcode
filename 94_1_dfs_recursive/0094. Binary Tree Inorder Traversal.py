# 1. DFS
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# 2. BFS
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
