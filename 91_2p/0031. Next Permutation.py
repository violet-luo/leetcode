def nextPermutation(self, nums: List[int]) -> None:
    n = len(nums)

    # 1. 从后往前找第一个降序元素 A[i]
    for i in range(n - 2, -1, -1):
        if nums[i + 1] > nums[i]:
            break
    else:
        nums.reverse()
        return nums

    # 2. 从后往前找第一个比 A[i] 大的元素 A[k]
    for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            break
    
    # 3. reverse A[i+1:]
    nums[i+1::] = nums[i+1:][::-1] # 不能只是nums[i+1:][::-1], 这个只是copy, 没有真的改变
    
###

def nextPermutation(self, nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        # find the index of the last peak
        if nums[i] > nums[i - 1]:
            # i = 3, [1,2,3,6,5,4] -> [1,2,3,4,5,6]
            nums[i:] = sorted(nums[i:])

            # swap the pre-last peak index with the value just larger than it
            # [1,2,3,4,5,6] -> [1,2,4,3,5,6]
            for j in range(i, n):
                if nums[i-1] < nums[j]:
                    nums[j], nums[i-1] = nums[i-1], nums[j]
                    return nums
                    
    # [3,2,1] -> [1,2,3]
    return nums.reverse()
