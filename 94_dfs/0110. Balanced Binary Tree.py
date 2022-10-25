def isBalanced(self, root):
    if not root:
        return True
   if not self.isBalanced(root.left):
        return False
    if not self.isBalanced(root.right):
        return False
        
    return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
    
def getHeight(self, node):
    if not node:
        return 0
    leftHeight = self.getHeight(node.left)
    rightHeight = self.getHeight(node.right)
    return max(leftHeight, leftHeight) + 1
