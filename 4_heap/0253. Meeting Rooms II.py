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
