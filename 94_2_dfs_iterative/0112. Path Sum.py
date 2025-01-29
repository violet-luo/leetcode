def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
        
    stack = [root]
    while stack:
        cur = stack.pop()
        if not cur.left and not cur.right and cur.val == targetSum:
            return True
        if cur.left:
            cur.left.val += cur.val
            stack.append(cur.left)
        if cur.right:
            cur.right.val += cur.val
            stack.append(cur.right)
    return False

###

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
