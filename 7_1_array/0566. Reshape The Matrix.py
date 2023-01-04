"""
Runtime: 100 ms, faster than 82.10% of Python3 online submissions for Reshape the Matrix.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Reshape the Matrix.
"""

def rotate(nums, r, c):
    flat_list = []
    matrix = []

    for sublist in nums:
        for item in sublist:
            flat_list.append(item)

    if len(flat_list) != r * c:
        return nums
    else:
        for i in range(0,len(flat_list),c):
            matrix.append(flat_list[i:i+c])
        return matrix
