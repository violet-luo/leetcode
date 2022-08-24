def twoSum(self, num: List[int], target: int) -> List[int]:
    if not num:
        return [-1, -1]
    
    l, r = 0, len(num) - 1
    
    while l < r:
        two_sum = num[l] + num[r]
        if two_sum == target:
            return [l+1, r+1] # 1-indexed
        elif two_sum < target:
            l += 1
        else:
            r -= 1
