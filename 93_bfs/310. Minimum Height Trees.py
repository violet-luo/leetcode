def findMinHeightTrees(self, n, edges):
    if n <= 2:
        return [i for i in range(n)]
    
    graph = self.buildGraph(n, edges)
    return self.topological_sort(n, graph)
    
# 标准拓扑排序模板
def topological_sort(self, n, graph):
    # 1. 统计每个点的入度
    indegrees = self.getIndegrees(n, graph)

    # 2. 将每个入度为1的点放入队列 queue 中作为起始节点
    queue = collections.deque([node for node in indegrees if indegrees[node] == 1])
            
    while queue:
        res, size = list(queue), len(queue)
        for _ in range(size):
            node = queue.popleft()
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 1:
                    queue.append(neighbor)
                    
    return res

def buildGraph(self, n, edges):
    graph = {i:set() for i in range(n)}
    
    for node, neighbor in edges:
        graph[node].add(neighbor)
        graph[neighbor].add(node)
    
    return graph

# 标准拓扑排序入度模板
# 统计每个点的入度。如果一个点的入度为0，那么这个点依然存在于dict中，对应入度为0
def getIndegrees(self, n, graph):
    indegrees = {node : 0 for node in range(n)}
    
    for node in graph:
        # 所有邻居的入度加1
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
    
    return indegrees
