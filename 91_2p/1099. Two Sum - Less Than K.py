def twoSumLessThanK(self, nums, k):
    if not nums:
        return -1
    
    nums.sort()
    l, r = 0, len(nums) - 1
    max_two_sum = -1
    
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum >= k:
            r -= 1
        else:
            l += 1
            max_two_sum = max(two_sum, max_two_sum) #而不是max_2sum = 2sum
    return max_two_sum
