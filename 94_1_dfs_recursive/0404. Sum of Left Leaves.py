def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def get_sum(node):
        if not node:
            return 0

        left_sum = get_sum(node.left)
        right_sum = get_sum(node.right)
        if node.left and not node.left.left and not node.left.right:
            left_sum += node.left.val
        return left_sum + right_sum

    return get_sum(root)
    
###

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
