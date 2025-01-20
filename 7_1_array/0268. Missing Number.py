def missingNumber(self, nums: List[int]) -> int:
    actual = sum(nums)
    expected = 0

    # for n in range(1, len(nums) + 1):
    #     expected += n
    
    expected = len(nums) * (len(nums) + 1) // 2

    return expected - actual
