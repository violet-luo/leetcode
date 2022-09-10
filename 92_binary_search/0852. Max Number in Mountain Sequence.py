def mountainSequence(nums):
    if not nums:
        return -1
        
    # 找到第一个符合条件nums[i] > nums[i+1]的i
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        # mid + 1一定不会越界
        # 因为 while 循环退出条件是 l + 1 < r
        # 所以一定有 l < mid + 1 < r
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid

    # 返回l和r中较大的值，则为山顶
    return max(nums[l], nums[r])
