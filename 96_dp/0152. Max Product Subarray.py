def maxProduct(self, nums: List[int]) -> int:
    if not nums:
        return None

    global_max = prev_max = prev_min = nums[0]

    for num in nums[1:]:
        if num > 0:
            cur_max = max(num, prev_max * num)
            cur_min = min(num, prev_min * num)
        else:
            cur_max = max(num, prev_min * num)
            cur_min = min(num, prev_max * num)

        global_max = max(global_max, cur_max)
        prev_max, prev_min = cur_max, cur_min

    return global_max

###

def maxProduct(self, nums):
    res = nums[0]
    min_p = max_p = nums[0]
    for i in range(1, len(nums)):
        tmp = min_p
        min_p = min(nums[i], min_p * nums[i], max_p * nums[i])
        max_p = max(nums[i], max_p * nums[i], tmp * nums[i])
        res = max(res, max_p)
    return res
