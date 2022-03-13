def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    return self.dfs(root.left) + self.dfs(root.right)

def dfs(self, node):
    if node is None:
        return 0
    return max(self.dfs(node.left), self.dfs(node.right)) + 1
