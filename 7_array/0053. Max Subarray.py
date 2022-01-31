def maxSubArray(self, nums):
    # maxAns记录全局最大值 sum记录当前子数组的和
    sum, maxSum = 0, -sys.maxsize
    # 贪心
    for num in nums:
        sum += num
        maxSum = max(maxSum, sum)
        sum = max(sum, 0)

    return maxSum
