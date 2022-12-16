import collections
def find_median_course(prereq_courses):
    # 1. 先建空图和空入度
    graph = collections.defaultdict(list) # {precourse: [all the following courses]} 
    indegree_map = collections.defaultdict(int) # {course: indegree}
    # 设全部课的入度为0
    for course_pair in prereq_courses:
        for course in course_pair:
            indegree_map[course] = 0
    
    # 2. 赋值图和入度
    for precourse, course in prereq_courses:
        graph[precourse].append(course)
        indegree_map[course] += 1
    
    # 3. 入度0加入queue
    queue = collections.deque()
    for course, indegree in indegree_map.items():
            if indegree == 0:
                queue.append(course)
                
    # 4. 遍历queue
    res = []
    while queue:
        cur_course = queue.popleft()
        res.append(cur_course)
        for following_course in graph[cur_course]:
            indegree_map[following_course] -= 1
            if indegree_map[following_course] == 0:
                queue.append(following_course)
    
    n = len(res)
    return res[n // 2] if len(res) % 2 == 1 else res[n // 2 - 1]
