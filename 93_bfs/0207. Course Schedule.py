def canFinish(self, numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]

    # 1. 统计每个点的入度，并构建图 
    in_degree = [0] * numCourses
    for node_in, node_out in prerequisites:
        graph[node_out].append(node_in) #存储每节课对应的后续课
        in_degree[node_in] += 1 #每节课加入度
    
    # 2. 将每个入度为0的点放入队列 queue 中作为起始节点
    queue = collections.deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    # 记录已修课程的数量
    num_choose = 0
    
    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        now_pos = queue.popleft()
        num_choose += 1
        # 将每条邻边删去，如果入度降为 0，再加入队列
        for j in graph[now_pos]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                queue.append(j)
    
    return num_choose == numCourses
