def searchRange(nums, target):
    if not nums:
        return [-1, -1]
        
    # 第一次二分查找第一个>= target的位置
    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 #上取整
            if nums[m] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1
    
    # 第二次二分查找最后一个 <= target的位置
    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1 # 下取整，防止死循环
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]
