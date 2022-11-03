def longestUnivaluePath(self, root):
    self.longest = 0
    self.dfs(root, None)
    return self.longest

def dfs(self, node, parent_val):
    if not node:
        return 0
    
    left = self.dfs(node.left, node.val)
    right = self.dfs(node.right, node.val)
    self.longest = max(self.longest, left + right)
    
    if node.val == parent_val:
        return 0
    else:
        return max(left, right) + 1
