def winSum(self, nums, k):
    if not nums or len(nums) < k:
        return []

    window_sum = sum(nums[:k])
    res = [window_sum]

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        res.append(window_sum)

    return res
