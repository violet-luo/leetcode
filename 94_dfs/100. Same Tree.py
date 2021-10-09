def isSameTree(self, p, q): 
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
       # if not p and not q: 两个都是空 return True 
       # if not p or not q: 只有一个是空 return False
        return p == q 
