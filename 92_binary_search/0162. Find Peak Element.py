def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid 
        elif nums[mid] > nums[mid + 1]:
            r = mid
        else:
            return mid

    if nums[l] > nums[r]:
        return l 
    return r

###

def findPeak(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = （l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
   return l
