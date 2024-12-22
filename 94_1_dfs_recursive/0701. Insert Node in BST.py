def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)
    def traverse(node) -> None:
        if node is None:
            return None
        if node.val < val: # no need to consider = because of BST
            if node.right is None:
                node.right = TreeNode(val)
            else:
                traverse(node.right)
        else:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                traverse(node.left)
    traverse(root)
    return root
    
###

def insertIntoBST(self, root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = self.insertIntoBST(root.left, val)
    else:
        root.right = self.insertIntoBST(root.right, val)
    return root
