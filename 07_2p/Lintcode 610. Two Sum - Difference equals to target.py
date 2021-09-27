def twoSum7(self, nums, target):
    if not nums:
        return [-1, -1]

    target = abs(target)
    j = 1
    for i in range(len(nums)):
        j = max(j, i+1)
        while j < len(nums) and nums[j] - nums[i] < target:
            j += 1
        if j >= len(nums):
            break
        if nums[j] - nums[i] == target:
            return [nums[i], nums[j]]

    return [-1, -1]
