def twoSum(self, numbers: List[int], target: int) -> List[int]:
    if not numbers:
        return [-1, 1]

    nums = [(number, index) for index, number in enumerate(numbers)]
    # nlogn
    nums.sort()

    # n
    left, right = 0, len(nums) - 1
    while left < right: # 需要两个数字所以没有等于
        if nums[left][0] + nums[right][0] > target:
            right -= 1
        elif nums[left][0] + nums[right][0] < target:
            left += 1
        else:
            return [nums[left][1], nums[right][1]]

    return [-1, 1]
