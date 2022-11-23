def topKFrequent(self, nums, k):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    heap = []
    for item in counts.items():
        heapq.heappush(heap, (-item[1], item[0]))

    results = []
    for i in range(k):
        count, value = heapq.heappop(heap)
        results.append(value)

    return results
