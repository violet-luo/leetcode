"""

Runtime: 92 ms, faster than 70.09% of Python3 online submissions for Merge Intervals.
Memory Usage: 15.5 MB, less than 92.55% of Python3 online submissions for Merge Intervals.

"""

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    # sort intervals by interval lower bound
    intervals.sort(key=lambda x:x[0]) 
    
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
