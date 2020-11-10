"""

Runtime: 28 ms, faster than 88.64% of Python3 online submissions for Remove Element.
Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Remove Element.

"""

def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
