def longestConsecutive(self, root):
    self.max_len = 0
    self.dfs(root, 1)
    return self.max_len

def dfs(self, root, length): 
    if not root:
        return 

    if root.left:
        if root.val + 1 == root.left.val:
            self.dfs(root.left, length + 1)
        else:
            self.dfs(root.left, 1)
    if root.right:
        if root.val + 1 == root.right.val:
            self.dfs(root.right, length + 1)
        else:
            self.dfs(root.right, 1)

    self.max_len = max(self.max_len, length)
