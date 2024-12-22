def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def rotate(x):
        if x is None:
            return None

        y = x.left
        z = x.right
        if y is None:
            return x
        new_left = rotate(y)

        y.right = x
        y.left = z
        x.left = None
        x.right = None
        return new_left

    return rotate(root)
