"""

Runtime: 84 ms, faster than 68.13% of Python3 online submissions for Insert Interval.
Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Insert Interval.

"""

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0 
    n = len(intervals)
    res = []

    while i < n and newInterval[0] > intervals[i][1]:
        res.append(intervals[i])
        i += 1
    tmp = [newInterval[0], newInterval[1]]

    while i < n and newInterval[1] >= intervals[i][0]:
        tmp[0] = min(tmp[0], intervals[i][0])
        tmp[1] = max(tmp[1], intervals[i][1])
        i += 1

    res.append(tmp)

    while i < n :
        res.append(intervals[i])
        i += 1

    return res
