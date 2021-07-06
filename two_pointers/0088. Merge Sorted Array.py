"""
  
Runtime: 36 ms, faster than 65.57% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 70.19% of Python3 online submissions for Merge Sorted Array.

http://www.pythontutor.com/visualize.html#code=def%20merge%28nums1,%20m,%20nums2,%20n%29%3A%0A%20%20%20%20p,%20p1,%20p2%20%3D%20m%20%2B%20n%20-%201,%20m%20-%201,%20n%20-%201%0A%0A%20%20%20%20while%20p1%20%3E%3D%200%20and%20p2%20%3E%3D%200%3A%0A%20%20%20%20%20%20%20%20if%20nums1%5Bp1%5D%20%3C%20nums2%5Bp2%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nums1%5Bp%5D%20%3D%20nums2%5Bp2%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20p2%20-%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nums1%5Bp%5D%20%3D%20nums1%5Bp1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20p1%20-%3D%201%0A%20%20%20%20%20%20%20%20p%20-%3D%201%0A%0A%20%20%20%20%23%20add%20missing%20elements%20from%20nums2%0A%20%20%20%20nums1%5B%3Ap2%20%2B%201%5D%20%3D%20nums2%5B%3Ap2%20%2B%201%5D%0A%20%20%20%20%0Amerge%28%5B1,2,3,0,0,0%5D,%203,%20%5B2,5,6%5D,%203%29&cumulative=false&curInstr=19&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
  
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
