def deduplication(self, nums):
    if not nums:
        return 0

    # time nlogn, uses quick sort which is in place
    nums.sort() 
    j = 1
    # time complexity O(n)
    for i in range(len(nums)):
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        if j >= len(nums):
            break
        nums[i + 1] = nums[j]

    return i + 1
