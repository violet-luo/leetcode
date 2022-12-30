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
