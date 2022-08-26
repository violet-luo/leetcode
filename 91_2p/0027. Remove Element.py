def removeElement(nums, val):
    l = 0
    for j in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l
