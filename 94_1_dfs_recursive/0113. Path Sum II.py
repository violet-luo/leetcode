def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []
    path = []

    def traverse(node, path_sum: int) -> None:
        if not node:
            return None
        
        path_sum += node.val
        path.append(node.val)
        
        if not node.left and not node.right and path_sum == targetSum:
            # path 只是 pointer to the actual subset, at the end subset will be []
            # path[:] creates shallow copy, create a snapshot of subset at that moment
            res.append(path[:])
        traverse(node.left, path_sum)
        traverse(node.right, path_sum)

        path.pop()
    
    traverse(root, 0)
    return res
    
###

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
