def findMin(self, nums):
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    
    # find the first element <= target
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            # 如果mid位置上的数字小于等于最右端的数字，区间向左移动
            start = mid 
        # 注意：题目声明不存在相等元素，所以这里else 等价于 mid < end
        else:
            end = mid

    return min(nums[start], nums[end])
