def kClosest(points, k):
    heap, res = [], [] #最小栈，栈顶放最近点

    for x, y in points:
        heapq.heappush(heap, [x ** 2 + y ** 2, x, y]) # dist/x/y小的优先

    for _ in range(k):
        _, x, y = heapq.heappop(heap)
        res.append([x, y])

    # 不可以是以下，因为其实heap并没有排序，要到push时才排序
    # for i in range(k):
        # res.append([heap[i][1], heap[i][2]])
    return res
