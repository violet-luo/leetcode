def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    res = []

    def traverse(node, path_sum):
        nonlocal res
        if not node:
            return None

        path_sum += node.val
        if not node.left and not node.right:
            res.append(path_sum)
        else:
            traverse(node.left, path_sum)
            traverse(node.right, path_sum)

    traverse(root, 0)
    return True if targetSum in res else False

###

def hasPathSum(self, root, sum):
    if not root: # 出口2，这里加not sum会死循环，报错
        return False
    if root.val == sum and not root.left and not root.right: # 出口1
        return True
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
