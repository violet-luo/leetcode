def merge(self, intervals):
    intervals.sort(key = lambda x:x[0])
    res = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    
    return res

###

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    # sort intervals by interval lower bound
    intervals.sort() 
    
    i = 0
    for interval in intervals:
        # if res is null or the last interval does not overlap with the current one
        # e.g. [1,2] [3,4]
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        # e.g. [1,3] [2,4] or [1,4] [2,3]
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res
