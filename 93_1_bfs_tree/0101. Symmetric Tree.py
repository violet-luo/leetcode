def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root or (not root.left and not root.right):
        return True
    if (root.left and not root.right) or (not root.left and root.right):
        return False
    queue = collections.deque([(root.left, root.right)])

    while queue:
        l, r = queue.popleft()
        if l.val != r.val:
            return False
        if (l.left and not r.right) or (l.right and not r.left) or (not l.left and r.right) or (not l.right and r.left):
            return False
        if l.left and r.right:
            queue.append((l.left, r.right))
        if l.right and r.left:
            queue.append((l.right, r.left))
    
    return True
    
###

def isSymmetric(self, root):
    if not root:
        return True
    queue = collections.deque([(root.left, root.right)])
    
    while queue:
        l, r = queue.popleft()
        if not l and not r:
            continue
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        queue.append((l.left, r.right))
        queue.append((l.right, r.left))
    return True
