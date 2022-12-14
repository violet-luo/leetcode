def diameterOfBinaryTree(self, root):
    return self.getHeight(root.left) + self.getHeight(root.right)
    
def getHeight(self, node):
    if not node:
        return 0
    leftHeight = self.getHeight(node.left)
    rightHeight = self.getHeight(node.right)
    return max(leftHeight, leftHeight) + 1
