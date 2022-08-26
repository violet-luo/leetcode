def removeElement(nums, val):
    l = 0
    for r in range(len(nums)): # 从0开始，因为第一个也可能要被Remove
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l
