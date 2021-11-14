def sequenceReconstruction(self, org, seqs):
    graph = self.build_graph(seqs)
    topo_order = self.topological_sort(graph)
    return topo_order == org

def build_graph(self, seqs): # [[1,2],[1,3]]
    graph = {}
    for seq in seqs:
        for node in seq:
            if node not in graph:
                graph[node] = set() # {1: set(), 2: set(), 3: set()}

    for seq in seqs:
        for i in range(1, len(seq)):
            graph[seq[i - 1]].add(seq[i]) # {1: {2, 3}, 2: set(), 3: set()}

    return graph 

# 标准拓扑排序模板
def topological_sort(self, graph):
    # 1. 统计每个点的入度
    indegree = self.get_indegree(graph)
    
    # 2. 将每个入度为0的点放入队列 queue 中作为起始节点
    queue = collections.deque([ node for node in nodes if indegree[node] == 0 ])
    topo_order = []
    
    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        # there must exist more than one top orders
        if len(queue) > 1:
            return None
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(graph): # 比模板多了这个判断
        return topo_order

    return None

# 标准拓扑排序入度模板
# 统计每个点的入度。如果一个点的入度为0，那么这个点依然存在于dict中，对应入度为0
def get_indegree(self, graph):
    # 初始化所有点的入度为0
    indegree = { node: 0 for node in graph }

    for node in graph:
        # 所有邻居的入度加1
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    return indegree
