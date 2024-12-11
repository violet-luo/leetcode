def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    max_diameter = 0

    def get_height(node):
        if not node:
            return 0
        nonlocal max_diameter
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        max_diameter = max(max_diameter, left_height + right_height)
        return max(left_height, right_height) + 1

    get_height(root)
    return max_diameter
