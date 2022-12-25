def threeSumClosest(nums, target):
    n = len(nums)
    if not nums or n < 3:
        return
    
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    
    for i in range(n):
        left, right = i + 1, n - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == target:
                return three_sum
            elif abs(three_sum - target) < abs(res - target): # 找不到exact match, return the closest match
                res = three_sum
            
            if three_sum < target:
                left += 1
            elif three_sum > target:
                right -= 1
                
    return res
