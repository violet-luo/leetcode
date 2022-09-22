def nextGreatestLetter(nums, target):
    if target >= nums[-1]:
        return nums[0]
    
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        # 这里要加 =
        # ["e","e","n"]，"e" => "n"
        if nums[mid] <= target: 
            l = mid
        else: 
            r = mid
    
    if nums[l] > target:
        return nums[l]
    
    return nums[r]
