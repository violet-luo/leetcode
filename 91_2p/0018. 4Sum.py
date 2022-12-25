def fourSum(self, nums, target):
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        # i去重，去重模版，如果当前元素和左边元素一样，跳过
        if i and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            # j去重，当j和i相等的时候，只记录第一个j, 试例[2,2,2,2,2], 8
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            two_sum = target - nums[i] - nums[j]
            # 同 three sum
            left, right = j + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == two_sum:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > two_sum:
                    right -= 1
                else:
                    left += 1
    return res
