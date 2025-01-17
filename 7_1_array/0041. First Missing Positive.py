def firstMissingPositive(self, nums: List[int]) -> int:  
    n = len(nums)
    i = 0
    
    while i < n:
        correct_idx = nums[i]-1 # 应该放的位置是 nums[i]-1，比如数字1应该在索引0上
        # 1 <= nums[i] <= n 当前数字是有效的正整数
        # 且当前数字没有在正确的位置上，交换
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        # 如果数字已经在正确的位置，或者是无效数字（如负数或大于 n 的数字）
        # 直接跳过当前索引，处理下一个数字
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1
