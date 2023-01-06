def twoSum(self, nums, target):
    num_to_idx = {} # 不用sort

    for i in range(len(nums)): # 不用for num in nums 因为最后return idx
        if target - nums[i] in num_to_idx:
            return [num_to_idx[target - nums[i]], i] # [i, num_to_idx[target - nums[i]] 也可以
        else:
            num_to_idx[nums[i]] = i
