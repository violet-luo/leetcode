def partitionArray(self, nums, k):
   if not nums:
        return 0
    
   l, r = 0, len(nums) - 1

    # if l < r, while 循环结束在l == r
    # 此时需要多一次 if 语句判断 nums[l] 到底是 <k 还是 >= k
    # 因此使用 l <= r 可以省去这个判断
    while l <= r:
        while l <= r and nums[l] < k:
            l += 1
        while l <= r and nums[r] >= k:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    return l
