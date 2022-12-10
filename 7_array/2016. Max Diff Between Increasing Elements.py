def maximumDifference(self, nums):
    n = len(nums)
    res = -1
    prefix_min = nums[0] #前序数组里最小的数

    for i in range(1, n):
        if nums[i] > prefix_min:
            res = max(res, nums[i] - prefix_min)
        else: # nums[i] <= prefix_min
            prefix_min = nums[i]
    
    return res
