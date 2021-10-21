import collections

def findOrder(self, numCourses, prereq):
    # 构建图，代表先修课->后修课的映射
    graph = [[] for i in range(numCourses)]

    # 1. 统计每个点的入度，并构建图
    in_degree = [0] * numCourses
    for node_in, node_out in prereq:
        graph[node_out].append(node_in) #存储每节课对应的后续课
        in_degree[node_in] += 1 #每节课加入度

    # 2. 将每个入度为0的点放入队列 queue 中作为起始节点
    queue = collections.deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    # 记录已修课程的数量
    num_choose = 0
    topo_order = []

    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        now_pos = queue.popleft()
        topo_order.append(now_pos)
        num_choose += 1
        # 当前点的所有邻居的入度-1.表示每个后修课的一门先修课已经完成
        for j in graph[now_pos]: #当前课
            in_degree[j] -= 1 #当前课后面一节课入度-1
            # 4. 一旦发现新的入度为0的点，丢回队列中
            # 表示一门后修课的所有先修课已经完成，可以被修了
            if in_degree[j] == 0:
                queue.append(j)
    # 如果全部课程已被修过，那么返回拓扑排序，否则返回空
    return topo_order if num_choose == numCourses else []
