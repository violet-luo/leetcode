def pathSum(self, root, sum):
    def get_path_sum(root, cur_sum, sum):
        if not root:
            return 
        if not root.left and not root.right and sum - root.val == 0:
            cur_sum += [root.val]
            res.append(cur_sum)
        get_path_sum(root.left, cur_sum + [root.val], sum - root.val)
        get_path_sum(root.right, cur_sum + [root.val], sum - root.val)

    res = []
    get_path_sum(root, [], sum)
    return res

###

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
