def maxPathSum(self, root):
    self.max_sum = float('-inf')
    self.helper(root)
    return self.max_sum 

def helper(self, root):
    if not root: 
        return 0

    left = self.helper(root.left)
    right = self.helper(root.right)

    self.max_sum = max(self.max_sum, root.val, root.val + left, root.val + right, root.val + left + right)
    return max(root.val, root.val + left, root.val + right)
