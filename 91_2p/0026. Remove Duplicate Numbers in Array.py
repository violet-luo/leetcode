def removeDuplicates(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1 # slow是index, 所以数量要+1
