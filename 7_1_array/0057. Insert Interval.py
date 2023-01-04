def insert(self, intervals, newInterval):
    n = len(intervals)
    res = []
    i = 0

    # 依次扫描区间数组，分三种情况
    # 1. 不重叠，且区间在新区间的左边
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # 2. 重叠，进行合并
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0]) # 更新左边界
        newInterval[1] = max(intervals[i][1], newInterval[1]) # 更新右边界
        i += 1
    res.append(newInterval) # 更新完成后加入res中

    # 3. 不重叠，且区间在新区间的右边
    while i < n: # and intervals[i][0] > newInterval[1]
        res.append(intervals[i])
        i += 1
    return res 
