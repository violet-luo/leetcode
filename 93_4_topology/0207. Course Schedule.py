def canFinish(self, numCourses: int, prereq) -> bool:
    # 1. 先建空图和空入度
    graph = collections.defaultdict(list)
    indegree = [0] * numCourses
    
    # 2. 赋值图和入度
    for course, precourse in prereq:
        graph[precourse].append(course)
        indegree[course] += 1
    
    # 3. 入度0加入queue
    queue = collections.deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    
    # 4. 遍历queue
    num_taken = 0
    while queue:
        cur_course = queue.popleft()
        num_taken += 1
        for j in graph[cur_course]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)

    return num_taken == numCourses

###

def canFinish(self, numCourses, prereq):
    # 构建图，代表先修课 -> 后修课的映射
    graph = [[] for i in range(numCourses)]

    # 1. 统计每个点的入度，并构建图 
    indegree = [0] * numCourses # [0, 0, 0, 0]
    for course, precourse in prereq:
        # graph 存储每节课对应的后续课
        graph[precourse].append(course) # [[1,2], [3], [3], []]
        # 每节课加入度
        indegree[course] += 1 # [0, 1, 1, 2]
    
    # 2. 将每个入度为0的点放入队列 queue 中作为起始节点
    queue = collections.deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    # 记录已修课程的数量
    num_taken = 0
    
    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        cur_course = queue.popleft()
        num_taken += 1
        # 当前课的所有后续课入度-1
        for j in graph[cur_course]: #当前课
            indegree[j] -= 1
            # 4. 一旦发现新的入度为0的点，丢回队列中
            # 表示一门后修课的所有先修课已经完成，可以被修了
            if indegree[j] == 0:
                queue.append(j)
    
    return num_taken == numCourses
