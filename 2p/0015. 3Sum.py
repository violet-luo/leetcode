def threeSum(self, nums):
    results = []
    
    if not nums or len(nums) < 3:
        return results
        
    nums.sort()
    
    length = len(nums)
    # 遍历三元组中的最小数
    for i in range(0, length - 2):
        # 经典去重套路
        # 如果当前元素和左边元素一样，跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # abc, a为i，在 i+1 到 len-1 间寻找 bc    
        left = i + 1
        right = length - 1
        target = -nums[i]
        # 用经典的two sum
        self.find_two_sum(nums, left, right, target, results)
    return results

# 带有去重逻辑的相向双指针Two Sum
# [-7, 2, 2, 3, 4, 5, 5]
def find_two_sums(nums, left, right, target, results):
    while left < right:
        # [2........5]
        if nums[left] + nums[right] == target:
            results.append([-target], nums[left], nums[right]])
            # 两边同时移动
            right -= 1
            left += 1
            # 如果左指针当前数字和左边数字相同，左指针向中间移动，跳过重复
            # [3, 4]
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        # 当前 sum 小于 target, 右移左指针，去找更大的sum
        elif nums[left] + nums[right] > target:
            right -= 1
        # 当前 sum 大于 target, 左移右指针，去找更小的sum
        else:
            left += 1
