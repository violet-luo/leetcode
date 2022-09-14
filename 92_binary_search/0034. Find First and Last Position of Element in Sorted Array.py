"""

Runtime: 84 ms, faster than 65.21% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

"""

def searchRange(self, nums: List[int], target: int) -> List[int]:
    # two binary searches for the begining and end of the range
    if not nums:
        return [-1, -1]

    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]
