def hasPathSum(self, root, sum):
    if not root: # 这里加not targetSum会报错
        return False
    if root.val == sum and not root.left and not root.right:
        return True
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
