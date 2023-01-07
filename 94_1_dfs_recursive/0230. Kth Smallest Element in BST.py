def kthSmallest(self, root, k):
    arr = self.inorder(root)
    return arr[k - 1]

def inorder(self, root):
    if not root:
        return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)
