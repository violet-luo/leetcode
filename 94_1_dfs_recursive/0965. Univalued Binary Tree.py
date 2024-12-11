def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    uni_value = root.val
    if root.left:
        if root.left.val != uni_value:
            return False
    if root.right:
        if root.right.val != uni_value:
            return False
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        
###

def isUnivalTree(self, root):
    if not root:
        return True
    if root.left:
        if root.left.val != root.val:
            return False
    if root.right:
        if root.right.val != root.val:
            return False
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
