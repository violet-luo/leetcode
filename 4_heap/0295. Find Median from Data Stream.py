class MedianFinder:
    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
		        # pop the smallest from right and pushes the negated to left
            heappush(self.left, -heappushpop(self.right, num))
        else:
            heappush(self.right, -heappushpop(self.right, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2
