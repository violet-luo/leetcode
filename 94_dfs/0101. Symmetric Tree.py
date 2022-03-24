def isSymmetric(self, root):
    if not root:
        return True
    return self.helper(root.left, root.right)
    
def symmetryChecker(self, l_root, r_root): # (2,2) #(3,3)
    if not l_root and not r_root:
        return True
    if not l_root or not r_root:
        return False
    if l_root.val != r_root.val:
        return False
        
    return self.symmetryChecker(l_root.left, r_root.right) and right self.symmetryChecker(l_root.right, r_root.left)
