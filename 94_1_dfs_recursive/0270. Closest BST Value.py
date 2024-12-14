def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    res = root.val

    def traverse(node):
        nonlocal res
        if not node:
            return None
        if abs(node.val - target) < abs(res - target) or (abs(node.val - target) == abs(res - target) and node.val < res):
            res = node.val
        if node.val < target:
            traverse(node.right)
        elif node.val > target:
            traverse(node.left)
        else:
            return

    traverse(root)
    return res
###

def closestValue(self, root, target):
    upper = root
    lower = root
    while root:
        if target > root.val:
            lower = root
            root = root.right
        elif target < root.val:
            upper = root
            root = root.left
        else:
            return root.val
    if abs(upper.val - target) <= abs(lower.val - target):
        return upper.val
    return lower.val
