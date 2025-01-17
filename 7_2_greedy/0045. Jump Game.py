def jump(self, nums: List[int]) -> int:
    jumps = 0
    l, r = 0, 0
    farthest = 0

    while r < len(nums) - 1:
        for i in range(l, r + 1): # r inclusive
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        jumps += 1
    
    return jumps
