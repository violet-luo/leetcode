#1. BFS
def binaryTreeToLists(self, root):
    if not root:
       return []
    
    queue = collections.deque([root])
    res = []
    
    dummy = ListNode(0)
    
    while queue:
        dummy.next = None
        cur = dummy
        for i in range(len(queue)):
            head = queue.popleft()
            cur.next = ListNode(head.val)
            cur = cur.next
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)  
        res.append(dummy.next)
    
    return res
  
  
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
