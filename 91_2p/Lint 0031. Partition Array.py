def partitionArray(self, nums, k):
   if not nums:
        return 0
    
   left, right = 0, len(nums) - 1

    # if left < right, while 循环结束在left == right
    # 此时需要多一次 if 语句判断 nums[left] 到底是 <k 还是 >= k
    # 因此使用 left <= right 可以省去这个判断
    while left <= right:
        while left <= right and nums[left] < k:
            left += 1
        while left <= right and nums[right] >= k: # 不加等号会报错
            right -= 1
            
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    return left
