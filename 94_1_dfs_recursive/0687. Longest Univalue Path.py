def longestUnivaluePath(self, root):
    maxLen = 0
    def get_path_len(node):
        nonlocal maxLen
        if not node:
            return 0

        left = get_path_len(node.left)
        right = get_path_len(node.right)

        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0

        maxLen = max(maxLen, left+right)
        return max(left, right)
    
    get_path_len(root)
    return maxLen
