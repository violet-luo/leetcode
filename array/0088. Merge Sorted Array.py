"""

Runtime: 32 ms, faster than 91.14% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.1 MB, less than 16.80% of Python3 online submissions for Merge Sorted Array.


"""
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while n > 0:
        if m <= 0 or nums2[n-1] >= nums1[m-1]:  
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        else:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
