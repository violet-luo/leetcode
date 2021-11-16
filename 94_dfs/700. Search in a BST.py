def searchBST(self, root, val):
    if not root:
        return None # 未找到值为val的节点
    if val < root.val:
        return self.searchBST(root.left, val) # val小于根节点值，在左子树中查找哦
    elif val > root.val:
        return self.searchBST(root.right, val) # val大于根节点值，在右子树中查找
    else:
        return root
