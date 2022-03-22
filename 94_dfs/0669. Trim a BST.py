def trimBST(self, root, min, max):
    if root is None:
        return root
    if root.val < min :
        return self.trimBST(root.right, min, max)
    elif root.val > max :
        return self.trimBST(root.left, min, max)
    else: # min < root < max
        root.left = self.trimBST(root.left, min, max)
        root.right = self.trimBST(root.right, min, max)
    return root
