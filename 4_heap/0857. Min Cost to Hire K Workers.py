def mincostToHireWorkers(self, quality, wage, k):
    # 排序：越小的单位薪资越前，如果相同，更小的工作质量在前
    # zip is used to join two tuples
    # 先得出[unit wage, quality]: [[7,0, 10], [2,5, 20], [6.0, 5]]
    # 排序后：[[2.5, 20], [6.0, 5], [7.0, 10]]
    workers = sorted([float(w) / q, q] for w, q in zip(wage, quality)) 

    min_cost = float('inf')
    team_quality = 0
    heap = []

    for unit_wage, quality in workers:
        # 使用相反数将小项堆变成大顶堆
        heapq.heappush(heap, -quality) # [-20, -5, -10]
        team_quality += quality # 统计队伍的总质量 #20 #25 #35
        if len(heap) > k: 
            team_quality += heapq.heappop(heap) #[-10, -5]
        if len(heap) == k: # 到第k个人的时候开始计算结果
            min_cost = min(min_cost, team_quality * unit_wage) #150 #105

    return min_cost
