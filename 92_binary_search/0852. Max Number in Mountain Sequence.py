def peakIndexInMountainArray(self, nums):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]: 
            l = mid
        elif nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid # r = mid也可以

    if nums[l] > nums[r]: 
        return l
    return r
