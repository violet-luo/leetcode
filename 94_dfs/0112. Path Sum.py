def hasPathSum(self, root, sum):
    if not root: # 出口2，这里加not sum会死循环，报错
        return False
    if root.val == sum and not root.left and not root.right: # 出口1
        return True
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
