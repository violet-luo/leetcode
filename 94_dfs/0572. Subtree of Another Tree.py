def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
        return True
    if (not root and subRoot) or (root and not subRoot):
        return False
    if root.val == subRoot.val and self.isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #not and

def isSameTree(self, p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    if p.val != q.val: #出口
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
