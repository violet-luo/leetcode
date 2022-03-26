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
