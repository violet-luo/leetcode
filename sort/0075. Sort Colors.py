"""

Runtime: 36 ms, faster than 57.80% of Python3 online submissions for Sort Colors.
Memory Usage: 14 MB, less than 13.99% of Python3 online submissions for Sort Colors.

"""

def sortColors(self, nums: List[int]) -> None:
    """
    Three pointers
     - p0: rightmost boundary of 0s
     - p2: leftmost boundary of 2s
     - curr
    Move the curr pointer
    When it hits 0, replace with nums[p0]
    When it hits 2, replace with nums[p2]
    """
    p0 = curr = 0 
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[curr], nums[p0] = nums[p0], nums[curr]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
