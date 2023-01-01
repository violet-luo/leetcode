def closestValue(self, root, target):
    def dfs(node):
        nonlocal res
        if not node:
            return
        if abs(node.val - target) < abs(res - target):
            res = node.val
        if node.val > target:
            dfs(node.left)
        elif node.val < target:
            dfs(node.right)
        return

    res = root.val
    dfs(root)
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
