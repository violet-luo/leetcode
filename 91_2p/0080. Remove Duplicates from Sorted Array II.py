"""

Runtime: 52 ms, faster than 77.17% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14.2 MB, less than 99.95% of Python3 online submissions for Remove Duplicates from Sorted Array II.

"""

def removeDuplicates(self, nums: List[int]) -> int:
    j, count = 1, 1

    # start from the second element
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[j] = nums[i]
            j += 1

    return j
