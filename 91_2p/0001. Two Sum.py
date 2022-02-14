def twoSum(self, numbers, target):
    if not numbers:
        return [-1, 1]
    
    nums = [
        (number, index) for index, number in enumerate(numbers)
    ]
    # nlogn
    nums.sort()
    
    # n
    left, right = 0, len(nums) - 1
    while left < right：
        if nums[left][0] + nums[right][0] > target:
            right -= 1
        elif nums[left][0] + nums[right][0] < target:
            left += 1
        else:
            return sorted(nums[left][1], nums[right][1]])
            
    return [-1, 1]
