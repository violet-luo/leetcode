def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    # 标准二分模版
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            r = mid # l = mid 也可以，[1,2,2,3] 2 插在哪个2都可以
    
    # 坑2：因为用 < 判定，所以先判定左边
    if target <= nums[l]: # [1,2], 2
        return l
    if target <= nums[r]: # [1,2], 2
        return r
    return len(nums) # [1, 2], 3
