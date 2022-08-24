def twoSum(numbers, target):
    if not numbers:
        return [-1, -1]
    
    # enumerate(["eat", "sleep") => [(0, 'eat'), (1, 'sleep')]
   # 这里的顺序不能变为(idx, num)因为sorted sort tuple的第一个element也就是num
    nums = [(num, idx) for idx, num in enumerate(numbers)]
   # O(nlogn)
    nums = sorted(nums)
    
    l, r = 0, len(nums) - 1
   
   # O(n)
   # 需要两个数字所以没有等于
    while l < r:
        two_sum = nums[l][0] + nums[r][0]
        if two_sum == target:
            return sorted([nums[l][1], nums[r][1]])
        elif two_sum < target:
            l += 1
        else:
            r -= 1
