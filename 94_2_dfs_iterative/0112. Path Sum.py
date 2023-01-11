def hasPathSum(self, root, targetSum):
    if not root:
        return False
    queue = collections.deque([root])
    while queue:
        curr = queue.popleft()
        if not curr.left and not curr.right and curr.val == targetSum:
            return True
        if curr.left:
            curr.left.val += curr.val
            queue.append(curr.left)
        if curr.right:
            curr.right.val += curr.val
            queue.append(curr.right)
    return False
