def removeDuplicates(nums):
    if not nums:
        return 0
    
    l = 0
    for r in range(len(nums)):
        if nums[l] == nums[r]:
            r += 1
        else:
            nums[l + 1] = nums[r]
            l += 1
            r += 1
    return l + 1
