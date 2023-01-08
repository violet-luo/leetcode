def sortArrayByParity(self, nums):
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums

###

def partitionArray(self, nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        while l <= r and nums[l] % 2 == 0:
            l += 1
        while l <= r and nums[r] % 2 == 1:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    return nums
