def two_sum7(self, nums, target):
    target = abs(target)
    left, right = 0, 1
    
    while right < len(nums):
        if left == right:
            right += 1
        if nums[right] - nums[left] > target:
            left += 1
        elif nums[right] - nums[left] < target:
            right += 1
        else:
            return [nums[left], nums[right]]
    return [-1, -1]
