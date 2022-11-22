def kClosest(points, k):
    heap = [] #最小栈，栈顶放最近点
    res = []

    for point in points:
        dist = point[0] ** 2 + point[1] ** 2
        heapq.heappush(heap, (dist, point[0], point[1])) # dist/x/y小的优先

    for _ in range(k):
        _, x, y = heapq.heappop(heap)
        res.append([x, y])

    return res
