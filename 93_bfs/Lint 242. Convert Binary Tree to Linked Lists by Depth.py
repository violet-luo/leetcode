#1. BFS
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
  
  
#2.DFS
def binaryTreeToLists(self, root):
    result = []
    self.dfs(root, 1, result)
    return result

def dfs(self, root, depth, result):
    if root is None:
        return
    node = ListNode(root.val)
    if len(result) < depth:
        result.append(node)
    else:
        node.next = result[depth-1]
        result[depth-1] = node
    
    self.dfs(root.right, depth + 1, result)
    self.dfs(root.left, depth + 1, result)
