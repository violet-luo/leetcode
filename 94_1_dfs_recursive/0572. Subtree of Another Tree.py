def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    has_same_subtree = False

    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
    def traverse(node):
        nonlocal has_same_subtree
        if not node:
            return None
        if isSameTree(node, subRoot):
            has_same_subtree = True
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return has_same_subtree

###

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root is None: # 这里不需要check subRoot is None, 因为反正也是 False
        return False
    if self.isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def isSameTree(self, p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
