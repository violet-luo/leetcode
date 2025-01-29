def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []

    q = [(root, str(root.val))]
    while q:
        cur, path = q.pop()
        if not cur.left and not cur.right:
            res.append(path)
        if cur.left:
            q.append([cur.left, path + '->' + str(cur.left.val)])
        if cur.right:
            q.append([cur.right, path + '->' + str(cur.right.val)])
    
    return res
