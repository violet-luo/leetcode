def intersection(self, nums1, nums2):
    res = set()

    for num in nums1:
        if num in nums2:
            res.add(num)
    
    return res
