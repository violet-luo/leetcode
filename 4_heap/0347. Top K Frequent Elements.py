def topKFrequent(self, nums, k):
    counter = collections.Counter(nums)
    import heapq
    heap, res = [], []

    for num, cnt in counter.items():
        heapq.heappush(heap, [-cnt, num])
    
    for i in range(k):
        cnt, num = heapq.heappop(heap)
        res.append(num)

    return res
