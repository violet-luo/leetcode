def maxSubArray(self, nums):
    prefix_sum, max_sum = 0, float('-inf')

    for num in nums:
        prefix_sum += num
        max_sum = max(max_sum, prefix_sum)
        # If sum is positive, it's possible to make the next value bigger, so we keep it
        # If sum is negative, it has no use to the next element, so we replace with 0
        prefix_sum = max(prefix_sum, 0)

    return max_sum
