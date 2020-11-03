"""

Runtime: 44 ms, faster than 71.30% of Python3 online submissions for Find Peak Element.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Find Peak Element.

"""

def findPeakElement(self, nums: List[int]) -> int:
    # 若该元素恰好位于降序序列，则说明峰值会在本元素的左边。我们将搜索空间缩小为 mid的左边(包括其本身)，并在左侧子数组上重复上述过程

    start, end = 0, len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        # 若该元素恰好位于降序序列或者一个局部下降坡度中
        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start
