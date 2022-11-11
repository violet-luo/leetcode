def longestConsecutive(self, nums):
    max_len = 0
    res = set()
    
    for num in nums:
        res.add(num)
    
    for low in nums:
        if low - 1 not in res: # 不加会TLE
            high = low + 1
            while high in res:
                high += 1
            max_len = max(max_len, high - low)
        
    return max_len
