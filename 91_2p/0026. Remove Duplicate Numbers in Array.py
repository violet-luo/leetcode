def removeDuplicates(self, nums: List[int]) -> int: # [1,2,2,3]
    slow, fast = 0, 0

    while fast < len(nums): # 走到len(nums) - 1, 即3
        if nums[slow] == nums[fast]:
            fast += 1
        else: # 不要用while
            nums[slow + 1] = nums[fast] # slow = 2, [1,2,3]
            slow += 1 # slow = 2
            fast += 1 # fast = 3
    return slow + 1

###

def removeDuplicates(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1 # slow是index, 所以数量要+1
