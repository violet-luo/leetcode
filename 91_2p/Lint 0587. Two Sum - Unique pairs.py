def two_sum6(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if not nums or n< 2:
        return 0

    nums.sort()
    count = 0
    left, right = 0, n - 1
    
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            count, left, right = count + 1, left + 1, right - 1 #这里左右移动下面才不会index out of range
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif two_sum > target:
            right -= 1
        else:
            left += 1
    
    return count

###

def twoSum6(nums, target):
    n = len(nums)
    if not nums or n < 2:
        return 0
    
    count = 0
    nums.sort()
    l, r = 0, n- 1
    seen_pair = (None, None)
    
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum == target:
            if (nums[l], nums[r]) != seen_pair:
                count += 1
            seen_pair = (nums[l], nums[r])
            l, r = l + 1, r - 1
        elif two_sum > target:
            r -= 1
        else:
            l += 1
    
    return count
