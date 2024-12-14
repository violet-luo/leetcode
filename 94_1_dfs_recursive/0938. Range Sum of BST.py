def rangeSumBST(self, root, low, high):
    if not root:
        return 0 
    if root.val < low:
        return self.rangeSumBST(root.right, low, high)
    elif root.val > high:
        return self.rangeSumBST(root.left, low, high)
    else: # low < root.val < high
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

###

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    sum = 0
    if root.val > low: # 需要访问左子树
        sum += self.rangeSumBST(root.left, low, high)
    if root.val < high:
        sum += self.rangeSumBST(root.right, low, high)
    if low <= root.val <= high:
        sum += root.val     
    return sum
