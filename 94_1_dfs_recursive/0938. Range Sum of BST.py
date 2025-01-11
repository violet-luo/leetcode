def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    total = 0
    def traverse(node):
        nonlocal total
        if node is None:
            return None
        
        if node.val < low:
            traverse(node.right)
        elif node.val > high:
            traverse(node.left)
        else:
            total += node.val
            traverse(node.left)
            traverse(node.right)
    
    traverse(root)
    return total
    
###

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
    total = 0
    if root.val > low: # 需要访问左子树
        total += self.rangeSumBST(root.left, low, high)
    if root.val < high:
        total += self.rangeSumBST(root.right, low, high)
    if low <= root.val <= high:
        total += root.val     
    return total
