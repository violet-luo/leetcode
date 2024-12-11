def minDepth(self, root: Optional[TreeNode]) -> int:
    def get_height(node):
        if not node:
            return 0
        if not node.right:
            return get_height(node.left) + 1
        if not node.left:
            return get_height(node.right) + 1
        return min(get_height(node.left), get_height(node.right)) + 1
        
    return get_height(root)
###

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
