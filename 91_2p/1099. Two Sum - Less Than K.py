def twoSumLessThanK(self, nums: List[int], k: int) -> int:
    if not nums:
        return -1

    res = float('-inf')
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum < k:
            res = max(res, two_sum)
            left += 1
        else:
            right -= 1

    if res != float('-inf'): # 不判断[10,20,30], 15会错，或是直接init res = -1
        return res
    return -1


def twoSumLessThanK(self, nums, k):
    if not nums:
        return -1
    
    nums.sort()
    l, r = 0, len(nums) - 1
    res = -1
    
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum >= k:
            r -= 1
        else:
            l += 1
            res = max(two_sum, res) #而不是max_2sum = 2sum
    return res
