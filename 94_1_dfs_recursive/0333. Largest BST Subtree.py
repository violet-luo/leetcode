def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    max_cnt = 0

    def traverse(node):
        nonlocal max_cnt
        if node is None:
            return True, float('inf'), float('-inf'), 0
        
        l_bst, l_min, l_max, l_cnt = traverse(node.left)
        r_bst, r_min, r_max, r_cnt  = traverse(node.right)
        cnt = l_cnt + r_cnt + 1

        if l_bst and r_bst and l_max < node.val < r_min:
            max_cnt = max(max_cnt, cnt)
            return True, min(node.val, l_min), max(node.val, r_max), cnt # 不能直接写 True, l_min, r_max 因为l_min刚开始是float('-inf')
        else:
            return False, 0, 0, 0

    traverse(root)
    return max_cnt

###

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
