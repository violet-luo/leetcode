"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

def topSort(graph):
    # 1. 统计每个点的入度
    indegree = get_indegree(graph)

    # 2. 将每个入度为0的点放入队列 queue 中作为起始节点
    queue = collections.deque([ node for node in nodes if indegree[node] == 0 ])
    order = []

    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in node.neighbors:
            indegree[neighbor] -= 1 #邻居入度-1
            if indegree[neighbor] == 0: #邻居入度为0时加入队列
                queue.append(neighbor)
    return order

# 统计每个点的入度。如果一个点的入度为0，那么这个点依然存在于dict中，对应入度为0
def get_indegree(graph):
    # 初始化所有点的入度为0
    indegree = {x: 0 for x in graph}

    for node in graph:
        # 所有邻居的入度加1
        for neighbor in node.neighbors:
            indegree[neighbor] += 1
    return indegree
