def mountainSequence(self, nums):
    if not nums:
        return -1
        
    # 找到第一个符合条件nums[i] > nums[i+1]的i
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        # mid + 1一定不会越界
        # 因为 while 循环退出条件是 start + 1 < end
        # 所以一定有 start < mid + 1 < end
        # 如果从mid点向右下方倾斜，山峰一定在左边，丢掉右边 
        if nums[mid] > nums[mid + 1]:
            end = mid
        # 如果从mid点向右上方倾斜，山峰一定在右边，丢掉左边
        else:
            start = mid

    # 返回start和end中较大的值，则为山顶
    return max(nums[start], nums[end])
