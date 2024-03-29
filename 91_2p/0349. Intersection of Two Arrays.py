def intersection(self, nums1, nums2):
    res = set()
    nums1.sort()
    nums2.sort()
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2): # i 和 j 是 index, 所以没有等号
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else: # nums1[i] == nums2[j]:
            res.add(nums1[i])
            i += 1
            j += 1

    return list(res)
