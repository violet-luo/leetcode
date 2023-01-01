def findSecondMinimumValue(self, root):
    res = [float('inf')]
    def traverse(node):
        if not node:
            return
        if root.val < node.val < res[0]:
            res[0] = node.val
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return -1 if res[0] == float('inf') else res[0]

###

def findSecondMinimumValue(self, root):
    self.res = -1
    self.dfs(root, root.val)
    return self.res

def dfs(self, root, node):
    if not root:
        return
    if root.val != node:
        if self.res == -1:
            self.res = root.val
        else:
            self.res = Math.min(self.ans, root.val)
        return
    self.dfs(root.left, root.val)
    self.dfs(root.right, root.val)
