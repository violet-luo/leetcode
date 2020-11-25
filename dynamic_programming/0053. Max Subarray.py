"""

1. DP
Runtime: 68 ms, faster than 33.39% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.8 MB, less than 79.55% of Python3 online submissions for Maximum Subarray.

"""
def maxSubArray(self, nums: List[int]) -> int:
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum
   
   
"""

2. Divide and Conquer
Runtime: 88 ms, faster than 6.72% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15.1 MB, less than 17.84% of Python3 online submissions for Maximum Subarray.

"""
def maxSubArray(self, nums):
    def divide_and_conquer(nums, i, j):
        if i == j-1:
            return nums[i],nums[i],nums[i],nums[i]

        # we will compute :
        # a which is max contiguous sum in nums[i:j] including the first value
        # m which is max contiguous sum in nums[i:j] anywhere 
        # b which is max contiguous sum in nums[i:j] including the last value
        # s which is the sum of all values in nums[i:j]

        # compute middle index to divide array in two halves
        i_mid = i+(j-i)//2

        # compute a, m, b, s for left half
        a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)

        # compute a, m, b, s for right half
        a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)

        # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
        a = max(a1, s1+a2)
        b = max(b2, s2+b1)
        m = max(m1,m2,b1+a2)
        s = s1+s2
        return a,m,b,s

    _,m,_,_ = divide_and_conquer(nums, 0, len(nums))
    return m
