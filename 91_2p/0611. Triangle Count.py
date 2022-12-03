def triangleCount(self, nums):
    nums.sort()
    
    res = 0
    for i in range(len(nums)):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                res += right - left
                right -= 1
            else:
                left += 1
    return res
