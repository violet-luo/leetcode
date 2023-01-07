# 1. DFS Recursive
def preorderTraversal(self, root):
    if not root:
        return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# 2. DFS Iterative
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
