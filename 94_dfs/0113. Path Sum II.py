def pathSum(self, root, targetSum):
    res = []
    path = [root.val]
    self.dfs(root, 0, targetSum, path, res)
    return res

def dfs(self, node, currSum, targetSum, path, res)
    if not root:
        return

    currSum += node.val
    if not node.left and not node.right and currSum == targetSum: #出口
        res.append(list(path))
        return 

    if node.left:
        path.append(node.left.val)
        self.dfs(node.left, currSum, targetSum, path, res)
        path.pop()

    if node.right:
        path.append(node.right.val)
        self.dfs(node.right, currSum, targetSum, path, res)
        path.pop()    
