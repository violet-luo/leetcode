def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 1. 建立graph, 从前课到后课
    # 2. 建立indegree, 显示每节课有多少前置课
    graph = collections.defaultdict(list) # {0: [1, 2], 1: [3], 2: [3]})
    indegree = collections.defaultdict(int) # {1: 1, 2: 1, 3: 2})

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
  
    # 3. 将每个入度为0的点放入队列 queue 中作为起始节点
    # in range(numCourses) 而不是 in graph, 因为prereqs might be []
    q = collections.deque([node for node in range(numCourses) if indegree[node] == 0]) 
    order = []

    while q:
        cur_course = q.popleft()
        order.append(cur_course)
        for next_course in graph[cur_course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                q.append(next_course)
    
    return order if len(order) == numCourses else [] #与207唯一不同
        
###

def findOrder(self, numCourses, prereq):
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
    order = [] #与LC 207/Lint 615唯一不同

    # 3. 不断从队列中拿出一个点，去掉这个点的所有连边，其他点的相应入度-1
    while queue:
        cur_course = queue.popleft()
        order.append(cur_course)
        num_taken += 1
        # 当前课的所有后续课入度-1
        for j in graph[cur_course]: #当前课
            indegree[j] -= 1 #当前课后面一节课入度-1
            # 4. 一旦发现新的入度为0的点，丢回队列中
            # 表示一门后修课的所有先修课已经完成，可以被修了
            if indegree[j] == 0:
                queue.append(j)
    # 如果全部课程已被修过，那么返回拓扑排序，否则返回空
    return order if num_taken == numCourses else []
