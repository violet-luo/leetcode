def binaryTreeToLists(self, root):
    result = []
    if root is None:
        return result
        
    import Queue
    queue = Queue.Queue()
    
    queue.put(root)
    
    dummy = ListNode(0)
    
    lastNode = None
    
    while not queue.empty():
        dummy.next = None
        lastNode = dummy
        size = queue.qsize()
        for i in xrange(size):
            head = queue.get()
            lastNode.next = ListNode(head.val)
            lastNode = lastNode.next

            if head.left is not None:
                queue.put(head.left)
            if head.right is not None:
                queue.put(head.right)
    
        result.append(dummy.next)
    
    return result
