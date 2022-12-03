def twoSumLessThanK(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_two_sum = -1
    
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum >= k:
            right -= 1
        else:
            left += 1
            max_two_sum = max(two_sum, max_two_sum) 
    return max_two_sum
