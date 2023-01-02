def countUnivalSubtrees(self, root):
    count = 0

    def dfs(root):
        if not root:
            return True
        l = dfs(root.left)
        r = dfs(root.right)
        # if both children are "True" and root.val is equal to both children's values if exist
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            nonlocal count
            count += 1
            return True
        return False

    dfs(root)
    return count

###

def countUnivalSubtrees(self, root):
    self.count = 0
    self.dfs(root)
    return self.count

def dfs(self, root):
    if not root:
        return True
    l = self.dfs(root.left)
    r = self.dfs(root.right)
    # if both children are "True" and root.val is equal to both children's values if exist
    if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
        self.count += 1
        return True
    return False
