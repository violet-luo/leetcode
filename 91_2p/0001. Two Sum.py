def twoSum(nums, target):
    # nlogn
    nums.sort()

    # n
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]

    return [-1, 1]
