def tree2str(self, root):
    if not root:
        return ''
    # 4
    if not root.left and not root.right:
        return str(root.val)
    # 2(4)
    if not root.right:
        return str(root.val) + '(' + self.tree2str(root.left) + ')'
    # 1(2)(3)
    return str(root.val) + '(' + self.tree2str(root.left) + ')(' + self.tree2str(root.right) + ')'
