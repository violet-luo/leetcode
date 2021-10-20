class UndirectedGraphNode:
   def __init__(self,x):
        self.label = x #1
        self.neighbors = [] #[2,4]

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        # 1. 找到所有点
        nodes = self.find_nodes_by_bfs(node)
        # 2. 复制所有点
        mapping = self.copy_nodes(nodes)
        # 3. 复制所有边
        self.copy_edges(nodes, mapping)

        return mapping[node]

    # 1. 找到所有点，标准宽搜
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node]) # [A,B,C,D]
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)

    # 2. 复制所有点
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node]=UndirectedGraphNode(node.label)
        return mapping # A => A'

    # 3. 复制所有边
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            # 旧点有哪些旧邻居，新点就有哪些新邻居
            # A' => B'C', B => A'D', C' => A'D', D' => B'C' 
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
