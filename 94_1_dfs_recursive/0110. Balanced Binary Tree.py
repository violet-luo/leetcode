def isBalanced(self, root: Optional[TreeNode]) -> bool:
    res = True
    def get_heights(node):
        if not node:
            return 0
        nonlocal res

        left_height = get_heights(node.left)
        right_height = get_heights(node.right)
        diff = abs(left_height - right_height)
        if diff > 1:
            res = False # 不能直接return False here因为和下面的return type不一样
        return max(left_height, right_height) + 1
    
    get_heights(root)
    return res
    
###

def isBalanced(self, root):
    if not root:
        return True
   if not self.isBalanced(root.left):
        return False
    if not self.isBalanced(root.right):
        return False
        
    return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1
    
def getHeight(self, node):
    if not node:
        return 0
    leftHeight = self.getHeight(node.left)
    rightHeight = self.getHeight(node.right)
    return max(leftHeight, leftHeight) + 1
