import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        val = None
        
        for _ in range(n):
            val = heapq.heappop(heap) # 弹出当前最小丑数
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor) # heapppush(heap, ele)

        return val
