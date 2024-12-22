def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def validate(node) -> (bool, min: int, max: int):
        if node is None:
            return True, float('inf'), float('-inf')
        
        left_is_valid, l_min, l_max = validate(node.left)
        right_is_valid, r_min, r_max = validate(node.right)
        
        if not (left_is_valid and right_is_valid and l_max < node.val < r_min):
            return False, 0, 0
        
        subtree_min = min(l_min, node.val)
        subtree_max = max(r_max, node.val)
        
        return True, subtree_min, subtree_max
    
    is_valid, _, _ = validate(root)
    return is_valid

###

def isValidBST(self, root):
    return self.check_bst(float('-inf'), root, float("inf"))

def check_bst(self, left, node, right):
    if not node:
        return True
    if not left < node.val < right:
        return False
    return self.check_bst(left, node.left, node.val) and self.check_bst(node.val, node.right, right)
