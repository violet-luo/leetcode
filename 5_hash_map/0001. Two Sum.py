def twoSum(self, nums, target):
    num_to_idx = {}

    for i in range(len(nums)):
        if target - nums[i] in num_to_idx:
            return [num_to_idx[target - nums[i]], i] 
        else:
            num_to_idx[nums[i]] = i
 
    return [-1, -1]
