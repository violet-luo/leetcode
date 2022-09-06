def minSubArrayLen(target, nums):
    l = 0
    arr_sum = 0
    arr_len = float('inf') # 不能用0，因为要保证数值没有被overwrite

    for r in range(len(nums)):
        arr_sum += nums[r]
        while arr_sum >= target:
            arr_len = min(arr_len, r - l + 1)
            arr_sum -= nums[l]
            l += 1

    return 0 if arr_len == float('inf') else arr_len
