def longestConsecutive(self, nums):
    nums = set(nums)
    max_len = 0

    for low in nums:
        if low - 1 not in nums: # 将时间复杂度从O(n^2)降到了O(n)
            high = low + 1 
            while high in nums:
                high += 1
            max_len = max(max_len, high - low)
        
    return max_len
