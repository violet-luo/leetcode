def findMin(self, nums): 
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]: 
            l = mid
        else:
            r = mid

    return(min(nums[l], nums[r]))
