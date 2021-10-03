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
