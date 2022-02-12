def max_subarray(nums):
    prefix_sum = 0 #记录前i个数的和
   max_sum = -sys.maxsize #全局最大值，如果全是负数就不能设为0
   min_prefix_sum = 0 #记录前i个数中0-k的最小值
    
    for num in nums:
        prefix_sum += num
       # 因为min_prefix_sum会出现在两个运算中，所以后更新
        max_sum = max(max_sum, prefix_sum - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum)
        
    return max_sum
