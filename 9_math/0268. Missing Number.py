def findMissing(self, nums):
    N = len(nums)
    expect_sum = (N * (N+1))//2
    return expect_sum - sum(nums)
