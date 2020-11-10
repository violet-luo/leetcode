"""

1. Two Pointers
Runtime: 76 ms, faster than 89.76% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 92.65% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""

def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


"""

2. Set
Runtime: 84 ms, faster than 86.34% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 11.43% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""

def removeDuplicates(self, nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)
