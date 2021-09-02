def fourSum(self, numbers, target):
    if not numbers:
        return []

    nums = sorted(numbers)
    results = []

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
                results.append([nums[i], nums[j], c, d])

    return results

def find_two_sum_pairs(self, nums, left, right, target):
    pairs = []
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            if not pairs or (nums[left], nums[right]) != pairs[-1]:
                pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
    return pairs
