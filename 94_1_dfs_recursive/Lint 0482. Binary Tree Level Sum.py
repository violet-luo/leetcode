def levelSum(self,root,level):
    if root is None:
        return 0
    elif level == 1:
        return root.val
    return self.levelSum(root.left, level - 1) + self.levelSum(root.right, level - 1)
