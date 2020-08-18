"""

Runtime: 80 ms, faster than 94.14% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.4 MB, less than 91.94% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""

def removeDuplicates(self, nums: List[int]) -> int:
    x = 1
    for i in range(len(nums)-1):
        if(nums[i]!=nums[i+1]):
            nums[x] = nums[i+1]
            x+=1
    return(x)



"""

Runtime: 84 ms, faster than 86.34% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 11.43% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""

def removeDuplicates(self, nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)
