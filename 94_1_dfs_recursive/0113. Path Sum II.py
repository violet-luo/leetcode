def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []

    def traverse(node, path, path_sum):
        if not node:
            return None

        # 不能是 path.append(node.val)
        # When you call path.append(node) in one recursive branch
        # it modifies the same list path used in other branches of the recursion.
        # 会需要backtrack
        new_path = path + [node.val]
        new_path_sum = path_sum + node.val
        if not node.left and not node.right and new_path_sum == targetSum:
            res.append(new_path)
        else:
            traverse(node.left, new_path, new_path_sum)
            traverse(node.right, new_path, new_path_sum)

    traverse(root, [], 0)
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
