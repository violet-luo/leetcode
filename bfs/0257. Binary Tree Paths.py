def binaryTreePaths(self, root):
    # 处理空树
    paths = []
    if not root:
        return paths
    if not root.left and not root.right:
        return [str(root.val)]

    #左子树
    for path in self.binaryTreePaths(root.left):
        paths.append(str(root.val) + "->" + path)
    #右子树
    for path in self.binaryTreePaths(root.right):
        paths.append(str(root.val) + "->" + path)

    return paths
