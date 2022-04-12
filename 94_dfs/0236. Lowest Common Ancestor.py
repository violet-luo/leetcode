def lowestCommonAncestor(self, root, A, B):
    if root is None:
        return None
    if root == A or root == B:
        return root
    left = self.lowestCommonAncestor(root.left, A, B)
    right = self.lowestCommonAncestor(root.right, A, B)
    if left and right:
        return root 
    if left:
        return left
    if right:
        return right 
    return None
