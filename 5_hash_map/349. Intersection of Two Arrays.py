def intersection(self, nums1, nums2):
    set1 = set(nums1)
    res = []

    for num in nums2:
        if num in set1:
            res.append(num)
            set1.remove(num)
    return res
