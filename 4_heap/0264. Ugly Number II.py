def nthUglyNumber(self, n):
    import heapq
    heap = [1]
    visited = set([1])
    
    for _ in range(n):
        min_ugly_num = heapq.heappop(heap) # 弹出当前最小丑数
        for factor in [2, 3, 5]:
            if min_ugly_num * factor not in visited:
                visited.add(min_ugly_num * factor)
                heapq.heappush(heap, min_ugly_num * factor) # heapppush(heap, ele)

    return min_ugly_num
