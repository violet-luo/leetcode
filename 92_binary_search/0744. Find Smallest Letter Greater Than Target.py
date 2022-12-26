def nextGreatestLetter(nums, target): # [1,2,2,3], 2
    if target >= nums[-1]:
        return nums[0]
    
    # 标准二分模版找last pos of target
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] <= target: 
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid

    """
    1 2 2 3
    l m   r
      l m r
        l r
    """
    if target < nums[l]: # [2,3]
        return nums[l]
    
    return nums[r]
