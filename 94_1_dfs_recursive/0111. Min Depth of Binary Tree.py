def minDepth(self, root):
    if not root:
        return 0
    leftDepth = self.minDepth(root.left)
    rightDepth = self.minDepth(root.right)
    if root.left and root.right:
        return min(leftDepth, rightDepth) + 1
    else:
        return max(leftDepth, rightDepth) + 1
    
###

def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    leftDepth = self.minDepth(root.left)
    rightDepth = self.minDepth(root.right)
    
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1 + rightDepth
    if root.right is None:
        return 1 + leftDepth

    return min(leftDepth, rightDepth) + 1
