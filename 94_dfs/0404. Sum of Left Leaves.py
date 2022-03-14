def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    sum_left = 0
    if root.left: 
        if not root.left.left and not root.left.right: #出口：左叶子节点
            sum_left += root.left.val
        else:
            sum_left += self.sumOfLeftLeaves(root.left)
    if root.right:
        sum_left += self.sumOfLeftLeaves(root.right)
    return sum_left
