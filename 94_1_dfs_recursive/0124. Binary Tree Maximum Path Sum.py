def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_sum = float('-inf')

    def traverse(node) -> int:
        nonlocal max_sum
        if not node:
            return 0
        
        left_max_sum = max(traverse(node.left), 0) # ignore paths with negative sums
        right_max_sum = max(traverse(node.right), 0)

        curr_sum = left_max_sum + right_max_sum + node.val
        max_sum = max(max_sum, curr_sum)

        return node.val + max(left_max_sum, right_max_sum) # return the max sum path ending at the current node

    traverse(root)
    return max_sum
###

def maxPathSum(self, root):
    max_sum = float('-inf')
    
    def dfs(root):
        if not root: 
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)
        nonlocal max_sum
        max_sum = max(max_sum, root.val, root.val + left, root.val + right, root.val + left + right)
        return max(root.val, root.val + left, root.val + right)

    dfs(root)
    return max_sum 

###

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
