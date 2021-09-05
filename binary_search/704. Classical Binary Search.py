def findPosition(self, nums, target):
    if len(nums) == 0 or nums == None:
        return -1

    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1

    # start < end的话，是两数相等才会退出，数字一样容易死循环
    # start + 1 防止死循环，循环退出时还剩两个数
    while start + 1 < end:
        # 防止溢出
        mid = start + (end - start) // 2
        if target == nums[mid]:
            return mid 
        elif target > nums[mid]:
            start = mid # or start = mid + 1
        else:
            end = mid # or end = mid - 1

    # 还剩两个数的时候会退出循环
    # 要在循环外加条件判断
    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start
    else:
        return -1
