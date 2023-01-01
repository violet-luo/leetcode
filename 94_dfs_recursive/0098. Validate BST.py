def isValidBST(self, root):
    return self.check_bst(float('-inf'), root, float("inf"))

def check_bst(self, left, node, right):
    if not node:
        return True
    if not left < node.val < right:
        return False
    return self.check_bst(left, node.left, node.val) and self.check_bst(node.val, node.right, right)
