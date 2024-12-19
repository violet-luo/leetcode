def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
    graph = self.build_graph(nums, sequences)
    order = self.topological_sort(graph, nums)
    return order == nums

def build_graph(self, nums, sequences):
    graph = defaultdict(set)
    for num in nums:
        graph[num] # {1: set(), 2: set(), 3: set()}

    for seq in sequences:
        for i in range(1, len(seq)):
            # graph存储每个点对应的后序点
            graph[seq[i - 1]].add(seq[i]) # {1: {2, 3}, 2: set(), 3: set()}

    return graph

# 标准拓扑排序模板
def topological_sort(self, graph, nums):
    indegree = self.get_indegree(graph)
    queue = collections.deque([num for num in nums if indegree[node] == 0 ])
    order = []
    
    while queue:
        # 优化：比模板多了这个判断
        # 如果queue里有超过一个节点，说明排序的结果有多种可能
        # e.g. nums = [1,2,3], seq = [[1,2],[1,3]]
        # 处理节点1时，queue = [2, 3], 排序不唯一
        if len(queue) > 1:
            return None
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == len(graph): # 比模板多了这个判断
        return order
    return None

def get_indegree(self, graph):
    indegree = { node: 0 for node in graph }
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree

### Lintcode

def sequenceReconstruction(self, org, seqs):
    graph = self.build_graph(seqs)
    order = self.topological_sort(graph)
    return order == org

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
    order = []
    
    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        # 比模板多了这个判断
        # 如果queue里有超过一个节点，说明在刚刚遍历图的那一层出现了不止一个节点，直接返回None和org比对为False就行了
        if len(queue) > 1:
            return None
        # 标准拓扑模板
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == len(graph): # 比模板多了这个判断
        return order

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
