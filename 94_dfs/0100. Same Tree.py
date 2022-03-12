❌❌❌❌❌❌❌❌❌
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (p is None and q is not None) or (p is not None and q is None) or p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

✅✅✅✅✅✅✅✅✅
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None: 
        return True
    if p and q and p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return False

def isSameTree(self, p, q):
    if (not p and q) or (not q and p) or (p and q and p.val != q.val):
        return False               
    elif p and q:
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    else:
        return True
