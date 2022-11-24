class Solution:
    def __init__(self, k):
        self.k = k
        self.min_heap = [] #从小到大

    def add(self, num):
        heapq.heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) #pop最小值

    def topk(self):
        return sorted(self.min_heap, reverse=True)
