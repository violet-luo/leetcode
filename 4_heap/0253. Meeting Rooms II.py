def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key = lambda x: x[0])

    end_times_min_heap = [intervals[0][1]]

    for interval in intervals[1:]:
		    # 会议的开始时间小于最早结束的会议时间，说明需要新的房间
        if interval[0] < end_times_min_heap[0]:
            heapq.heappush(end_times_min_heap, interval[1])
        else: # 会议的开始时间大于等于最早结束的会议时间，更新最晚结束时间
            heapq.heappop(end_times_min_heap)
            heapq.heappush(end_times_min_heap, interval[1])
    return len(end_times_min_heap)
    
###

def minMeetingRooms(self, intervals): # [[0,30],[5,10],[15,20]]
    intervals.sort(key = lambda x: x[0]) # 按照开始时间排序，[[0,30],[5,10],[15,20]]

    import heapq
    heap = []
    heapq.heappush(heap, intervals[0][1]) # 加入第一个会议结束时间，heap = [30]
    for i in range(1, len(intervals)):
        if intervals[i][0] < heap[0]: # 第二个会议开始时间 < 第一个会议结束时间
            heapq.heappush(heap, intervals[i][1]) # 加入第二个会议结束时间，heap = [10, 30]
        else: # 第三个会议开始时间 > 第二个会议结束时间
            heapq.heappop(heap) 
            heapq.heappush(heap, intervals[i][1]) # 更新第三个会议结束时间，heap = [20, 30]
    return len(heap)
