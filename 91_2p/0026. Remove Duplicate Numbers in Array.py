def removeDuplicates(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1 # slow是index, 所以数量要+1

###

def removeDuplicates(nums):
    slow, fast = 0, 1

    while fast < len(nums):
        if nums[fast] != nums[slow]:
            nums[slow + 1] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    return slow + 1 # slow是index, 所以数量要+1
