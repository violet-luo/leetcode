def maxDiff(nums):
    max_diff = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] - nums[i] > max_diff:
                max_diff = nums[j] - nums[i]
    return max_diff
