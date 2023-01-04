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
