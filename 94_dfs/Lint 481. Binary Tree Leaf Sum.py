def leafSum(self, root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return self.leafSum(root.left) + self.leafSum(root.right)
