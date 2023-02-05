def deleteNode(self, root, key):
    if root is None:
        return None
    if key > root.val:  # 去右子树删除
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:  # 去左子树删除
        root.left = self.deleteNode(root.left, key)
    # 当前节点就是要删除的节点
    else:
        if root.left is None:  # 当前节点无左子树
            return root.right
        # 当前节点无右子树
        if root.right is None:
            return root.left
        # 当前节点左右子树都有
        node = root.right
        while node.left:  # 寻找欲删除节点右子树的最左节点
            node = node.left
        node.left = root.left  # 将欲删除节点的左子树成为其右子树最左节点的左子树
        root = root.right  # 欲删除节点的右子树顶替其位置，节点被删除
    return root
