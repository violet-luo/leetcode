def kthLargestElement(self, nums, k):
    if not nums or k < 1 or len(nums) < k:
        return None
    # 把第 k 大元素的索引转换成从 0 开始的目标索引，即 len(nums) - k。比如最大的元素 k = 1, 索引是 len(nums) - 1
    target_index = len(nums) - k
    return self.partition(nums, 0, len(nums) - 1, target_index) 

# 标准快搜
def partition(self, nums, start, end, k):
   if start == end: # 只有一个元素时直接返回
        return nums[k]
        
    left, right = start, end
    pivot = nums[(start + end) // 2]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
            
    # 如果索引k小于索引right，搜索左侧
    if k <= right:
        return self.partition(nums, start, right, k)
    if k >= left:
        return self.partition(nums, left, end, k)
    
    return nums[k]
