def largestBSTSubtree(self, root: TreeNode) -> int:
    if root is None:
        return 0
    _, size, _, _ = self.helper(root)
    return size

def helper(self, root):
    if root is None:
        return True, 0, sys.maxsize, -sys.maxsize

    l_bst, l_size, l_min, l_max = self.helper(root.left)
    r_bst, r_size, r_min, r_max = self.helper(root.right)

    bst = l_bst and r_bst and root.val > l_max and root.val < r_min

    if bst:
        size = l_size + r_size + 1
    else:
        size = max(l_size, r_size)

    return bst, size, min(l_min, r_min, root.val), max(l_max, r_max, root.val)
