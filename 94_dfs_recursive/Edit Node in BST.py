def updateBSTBST(root, target, val):
    if not root:
        return  # 未找到target节点
    if target < root.val:
        updateBST(root.left, target, val) # target小于根节点值，在左子树中查找哦
    elif target > root.val:
        updateBST(root.right, target, val) # target大于根节点值，在右子树中查找
    else:  # 找到了
        root.val = val
