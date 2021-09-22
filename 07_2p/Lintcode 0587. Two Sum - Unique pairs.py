def twoSum6(self, nums, target):
    if not nums or len(nums) < 2:
        return 0

    nums.sort()

    count = 0
    left, right = 0, len(nums) - 1
    last_pair = (None, None)

    while left < right:
        if nums[left] + nums[right] == target:
            if (nums[left], nums[right]) != last_pair:
                count += 1
            last_pair = (nums[left], nums[right])
            left, right = left + 1, right - 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

    return count
