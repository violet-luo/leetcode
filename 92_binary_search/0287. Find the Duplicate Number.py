"""

1. Binary Search

"""
def findDuplicate(self, nums):
    start, end = 1, len(nums) - 1
    
    while start + 1 < end:
        mid = (start + end) // 2
        if self.smaller_than_or_equal_to(nums, mid) > mid:
            end = mid
        else:
            start = mid
            
    if self.smaller_than_or_equal_to(nums, start) > start:
        return start
        
    return end
    
def smaller_than_or_equal_to(self, nums, val):
    count = 0
    for num in nums:
        if num <= val:
            count += 1
    return count

###

def findDuplicate(nums):
    l, r = 1, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1

        # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，此时重复元素一定出现在 [1, 4] 区间里
        if cnt > mid:
            r = mid
        else:
            l = mid + 1

    return l
        

"""

2. Sort

Runtime: 68 ms, faster than 48.62% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 16.5 MB, less than 18.23% of Python3 online submissions for Find the Duplicate Number.

Time Complexity: sort takes O(nlogn)
Space Complexity: O(1)

"""

def findDuplicate(self, nums: List[int]) -> int:
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return nums[i]
   
   
"""

3. Set

Runtime: 52 ms, faster than 99.18% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 18.1 MB, less than 18.23% of Python3 online submissions for Find the Duplicate Number.

Time Complexity: O(n)
Space Complexity: O(n)

"""

def findDuplicate(self, nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
            seen.add(num)
