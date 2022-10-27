def sumOfLeftLeaves(self, root):
    if not root:
        return 0
    left_sum = 0
    if root.left: 
        if not root.left.left and not root.left.right: #出口：左叶子节点
            left_sum += root.left.val
        else:
            left_sum += self.sumOfLeftLeaves(root.left)
    if root.right: #如果不加这个条件就走不到15
        left_sum += self.sumOfLeftLeaves(root.right)
    return left_sum
