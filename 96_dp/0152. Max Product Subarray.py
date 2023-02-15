def maxProduct(self, nums):
    res = nums[0]
    min_p = max_p = nums[0]
    for i in range(1, len(nums)):
        tmp = min_p
        min_p = min(nums[i], min_p * nums[i], max_p * nums[i])
        max_p = max(nums[i], max_p * nums[i], tmp * nums[i])
        res = max(res, max_p)
    return res
