def totalOccurrence(self, nums, target):
    if not nums:
        return 0

    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            r = mid
    if nums[l] == target:
        first = l
    elif nums[r] == target:
        first = r

    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else: 
            l = mid

    if nums[r] == target:
        last = r
    elif nums[l] == target:
        last = l

    return last - first + 1
