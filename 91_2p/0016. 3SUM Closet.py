def threeSumClosest(self, nums, target):
    n = len(nums)
    if n < 3:
        return 
    
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            # 如果找不到exact match, return the closest match
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
    return res
