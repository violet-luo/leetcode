def fourSum(self, numbers, target):
    res = []
    if not numbers:
        return res

    nums = sorted(numbers)

    for i in range(len(nums)):
        # 经典去重套路
        # 如果当前元素和左边元素一样，跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 在 j+1 到 len(nums)-1 的区间寻找 (c,d)
            pairs = self.find_two_sum_pairs(
                nums, 
                j+1, 
                len(nums) - 1, 
                target - nums[i] - nums[j]
            )

            for (c, d) in pairs:
                res.append([nums[i], nums[j], c, d])

    return res

def find_two_sum_pairs(self, nums, l, r, target):
    pairs = []
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            if not pairs or (nums[l], nums[r]) != pairs[-1]:
                pairs.append((nums[l], nums[r]))
            l += 1
            r -= 1
    return pairs
