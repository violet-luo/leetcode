def subarraySum(self, nums, k):
    count = 0 
    prefix_sum = 0
    prefix_sum_to_count = collections.defaultdict(int)
    prefix_sum_to_count[0] = 1
    
    for num in nums:
        prefix_sum += num 
        if prefix_sum - k in prefix_sum_to_count: # 所以要初始化dic = {0:1}
            count += prefix_sum_to_count[prefix_sum - k]
        prefix_sum_to_count[prefix_sum] += 1

    return count
