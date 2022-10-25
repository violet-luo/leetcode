def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    return self.getHeight(root.left) + self.getHeight(root.right)

def getHeight(self, node):
    if not node:
        return 0
    return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
