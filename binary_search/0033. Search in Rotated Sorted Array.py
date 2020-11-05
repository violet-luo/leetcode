"""

Runtime: 36 ms, faster than 88.29% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.3 MB, less than 16.47% of Python3 online submissions for Search in Rotated Sorted Array.

"""

def search(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        # determine it's left rotated or right rotated
        if nums[mid] >= nums[start]: # left rotated, mid >= left, [3,4,5,6,7,1,2]
            if nums[start] <= target and target <= nums[mid]: # search in the left side [3,4,5]
                end = mid - 1
            else:
                start = mid + 1
        else: # right rotated, mid < left, [6,7,1,2,3,4,5]
            if nums[mid] <= target <= nums[end]: # search in the right side [2,3,4,5]
                start = mid + 1
            else:
                end = mid - 1

    return -1
