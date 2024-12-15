def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    total = 0
    
    def traverse(node) -> int:
        nonlocal total
        if not node:
            return 0

        traverse(node.right) #走到最右叶子
        
        total += node.val
        node.val = total
        
        traverse(node.left)
    
    traverse(root)
    return root

###

def convertBST(self, root):
    self.sum = 0
    self.dfs(root)
    return root

def dfs(self, root):
    if root is None:
        return
    if root.right: # 走到最右叶子
        self.dfs(root.right)
    
    self.sum += root.val
    root.val = self.sum
    if root.left:
        self.dfs(root.left)
