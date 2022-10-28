def trimBST(self, root, low, high):
    if root is None:
        return
    if root.val < low:
        return self.trimBST(root.right, low, high)
    elif root.val > high:
        return self.trimBST(root.left, low, high)
    else: # min < root < max
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
    return root
