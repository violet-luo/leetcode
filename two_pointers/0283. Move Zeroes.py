"""

Runtime: 40 ms, faster than 97.12% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Move Zeroes.

"""

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1
