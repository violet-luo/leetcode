"""

Runtime: 232 ms, faster than 65.92% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.1 MB, less than 52.02% of Python3 online submissions for Product of Array Except Self.

"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    p = 1
    n = len(nums)
    output = []

    # get the product before the element 
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]

    # get the product after the element.
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output
