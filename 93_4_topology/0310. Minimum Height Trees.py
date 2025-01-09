def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2:
        return [i for i in range(n)]
    graph = collections.defaultdict(list) # graph = {3: [0, 1, 2, 4], 0: [3], 1: [3], 2: [3], 4: [3, 5], 5: [4]}
    indegree = collections.defaultdict(int) # indegree = {3: 4, 0: 1, 1: 1, 2: 1, 4: 2, 5: 1}

    for node, neighbor in edges:
        graph[node].append(neighbor)
        graph[neighbor].append(node)
        indegree[node] += 1
        indegree[neighbor] += 1
    
    # 2. 将每个入度为1的点放入队列 queue
    q = collections.deque([node for node in indegree if indegree[node] == 1]) # q = [0, 1, 2, 5], q = [3, 4]
    while q:
        res = list(q) # [3, 4] # [4]
        # 和之前不同. 如果不加这一行，处理完3, 4变成了下一层
        # [3, 4], {3: 1, 0: 1, 1: 1, 2: 1, 4: 1, 5: 1})
        # [4], {3: 1, 0: 0, 1: 0, 2: 0, 4: 0, 5: 1})
        for _ in range(len(q)): 
            node = q.popleft() # 3
            for neighbor in graph[node]:
                indegree[neighbor] -= 1 # {4: 0}
                if indegree[neighbor] == 1:
                    q.append(neighbor)
    
    return res

###

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

###

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
