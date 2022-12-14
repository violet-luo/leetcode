def searchBST(root, val):
    if not root:
        return None
    if val == root.val:
        return root
    elif val < root.val:
        return self.searchBST(root.left, val)
    else:
        return self.searchBST(root.right, val)
