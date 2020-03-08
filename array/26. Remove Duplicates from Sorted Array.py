”“”
Runtime: 84 ms, faster than 76.69% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.5 MB, less than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
“”“


def removeDuplicates(nums):    
    nums[:] = sorted(set(nums))
    return len(nums)
