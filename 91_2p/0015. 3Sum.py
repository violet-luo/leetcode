def threeSum(self, nums):
    n = len(nums)
    if not nums or n < 3:
        return res
    nums.sort()
    res = []
    
    for i in range(n):
        # i去重，去重模版，如果当前元素和左边元素一样，跳过
        if i and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # left, right 去重
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif three_sum < 0:
                left += 1
            else:
                right -= 1
    return res
