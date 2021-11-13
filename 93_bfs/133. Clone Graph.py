class UndirectedGraphNode:
   def __init__(self,x):
        self.label = x #1
        self.neighbors = [] #[2,4]

class Solution:
    def cloneGraph(self, node):
       root = node # node之后会变，一定要copy一份
       if not node:
           return None

       # 1. 找到所有点
       nodes = self.getNodes(node)

       # 2. 复制所有点，将 旧->新 mapping存入哈希表
       mapping = {}
       for node in nodes:
           mapping[node] = UndirectedGraphNode(node.label) # A => A'

       # 3. 复制所有边/neighbors
       for node in nodes:
           new_node = mapping[node] # A => A'
           # 旧点有哪些旧邻居，新点就有哪些新邻居
           # A' => B'C', B => A'D', C' => A'D', D' => B'C'
           for neighbor in node.neighbors:
               new_neighbor = mapping[neighbor]
               new_node.neighbors.append(new_neighbor)

       return mapping[root]

   # 1. 找到所有点，标准宽搜
   def getNodes(self, node):
       queue = collections.deque([node])
       res = set([node]) # [A,B,C,D]
       while queue:
           head = queue.popleft()
           for neighbor in head.neighbors:
               if neighbor not in res:
                   res.add(neighbor)
                   queue.append(neighbor)
       return res
