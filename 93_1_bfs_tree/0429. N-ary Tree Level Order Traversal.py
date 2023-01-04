"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            level = []
            for i in range(len(queue)): 
                node = queue.popleft()
                level.append(node.label)
                for neighbor in node.neighbors:
                    queue.append(neighbor)
            res.append(level)
        return res
