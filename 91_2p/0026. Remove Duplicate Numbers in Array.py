def removeDuplicates(self, nums):
    slow = 0
    
    for fast in range(1, len(nums)): # range(len(nums)) 也可以
        if nums[slow] == nums[fast]:
            fast += 1
        else: # 走到第一个不一样的
            nums[slow + 1] = nums[fast]
            slow += 1
            fast += 1
    return slow + 1 # slow是index, 所以数量要+1
