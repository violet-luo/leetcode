"""

1. Two Pointers (front to end)

"""

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_copy = nums1[:m]
    nums1[:] = []

    p1, p2 = 0, 0



    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements left
    if p1 < m:
        nums1[p1+p2:] = nums1_copy[p1:]
    else:
        nums1[p1+p2:] = nums2[p2:]
     
     
"""
  
Runtime: 36 ms, faster than 65.57% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 70.19% of Python3 online submissions for Merge Sorted Array.
  
"""
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p, p1, p2 = m + n - 1, m - 1, n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
