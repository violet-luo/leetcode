def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    res = None
    def traverse(node):
        nonlocal res, k
        if not node:
            return
        
        traverse(node.left)
        k -= 1
        if k == 0:
            res = node.val
            return
        traverse(node.right)
    
    traverse(root)
    return res

###

def kthSmallest(self, root, k):
    arr = self.inorder(root)
    return arr[k - 1]

def inorder(self, root):
    if not root:
        return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)
