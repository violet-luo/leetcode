"""

Runtime: 36 ms, faster than 85.60% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.4 MB, less than 6.92% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

"""

def findMin(self, nums: List[int]) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid

    return nums[start]
