def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def distance(point):
        return point[0] ** 2 + point[1] ** 2
    
    def sort(start, end, k):
        if start >= end:
            return
        
        left, right = start, end
        pivot = distance(points[(start + end) // 2])

        while left <= right:
            while left <= right and distance(points[left]) < pivot:
                left += 1
            while left <= right and distance(points[right]) > pivot:
                right -= 1
            if left <= right:
                points[left], points[right] = points[right], points[left]
                left, right = left + 1, right - 1
        
        if k - 1 <= right: # 如果第k个点在左边
            sort(start, right, k)
        if k - 1 >= left:
            sort(left, end, k)
    
    sort(0, len(points) - 1, k)
    return points[:k]
