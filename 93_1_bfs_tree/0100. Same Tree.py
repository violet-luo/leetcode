def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False

    queue = collections.deque([(p, q)])
    while queue:
        l, r = queue.popleft()
        if l.val != r.val:
            return False
        if (l.left and not r.left) or (l.right and not r.right) or (not l.left and r.left) or (not l.right and r.right):
            return False
        if l.left and r.left:
            queue.append((l.left, r.left))
        if l.right and r.right:
            queue.append((l.right, r.right))

    return True
    
###

def isSameTree(self, p, q):
    queue = collections.deque([(p, q)])
    while queue:
        node1, node2 = queue.popleft()
        if not node1 and not node2:
            continue
        elif not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        queue.append((node1.right, node2.right))
        queue.append((node1.left, node2.left))
    return True
