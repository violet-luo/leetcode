def pathSum(self, root, targetSum):
    res = []

    def get_path_sum(root, targetSum, path):
        if not root:
            return
        if not root.left and not root.right and root.val == targetSum:
            res.append(path + [root.val])
        get_path_sum(root.left, targetSum - root.val, path + [root.val])
        get_path_sum(root.right, targetSum - root.val, path + [root.val])
    
    get_path_sum(root, targetSum, [])
    return res
