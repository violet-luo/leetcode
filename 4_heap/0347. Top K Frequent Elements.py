def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    min_heap = []
    counter = collections.Counter(nums)

    for num, count in counter.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return [num for (_, num) in min_heap]

###

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
