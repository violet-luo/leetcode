def removeElement(nums, val):
    count = 0
    for num in nums:
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count
