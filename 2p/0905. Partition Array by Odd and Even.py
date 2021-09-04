def partitionArray(self, nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        while start <= end and nums[start] % 2 == 1:
            start += 1
        while start <= end and nums[end] % 2 == 0:
            end -= 1
        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
