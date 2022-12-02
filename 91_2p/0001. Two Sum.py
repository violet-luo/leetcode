def twoSum(self, nums: List[int], target: int) -> List[int]:
    # enumerate(["eat", "sleep") => [(0, 'eat'), (1, 'sleep')]
    # 这里的顺序不能变为(idx, num)因为sorted sort tuple的第一个element也就是num
    nums = [(num, idx) for idx, num in enumerate(nums)]
    # O(nlogn)
    nums.sort()
    
    left, right = 0, len(nums) - 1
    
    # O(n)
    while left < right: # 需要两个数字所以没有等于
        two_sum = nums[left][0] + nums[right][0]
        if two_sum == target:
            return sorted([nums[left][1], nums[right][1]]) # return idx 而不是 return [left, right]
        elif two_sum > target:
            right -= 1
        else:
            left += 1
