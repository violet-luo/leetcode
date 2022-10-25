def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return self.isSameTree(root.left, root.right)

def isSameTree(self, p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
