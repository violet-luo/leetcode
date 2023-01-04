def nextGreaterElement(self, nums1, nums2): # [4,1,2] [1,3,4,2]
    res = {}
    stack = []
    # 因为nums1 是 nums2的子集，所以从后遍历nums2找后面比前面大的数
    for num in reversed(nums2): # 2
        while stack and num >= stack[-1]:
            stack.pop() # 弹走小的数
        res[num] = stack[-1] if stack else -1 # 这个元素身后的第一个高个 #{2:-1}
        stack.append(num)
        
    return [res[num] for num in nums1]
