"""

Runtime: 1056 ms, faster than 14.24% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 18.6 MB, less than 7.70% of Python3 online submissions for Kth Largest Element in an Array.

https://www.jiuzhang.com/solution/kth-largest-element/#tag-lang-python

"""

def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # convert the kth largest to the kth smallest
        k = n - k
        return self.partition(nums, 0, n - 1, k)
    
    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # if the kth smallest is on the right side, search the right side
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        return nums[k]
