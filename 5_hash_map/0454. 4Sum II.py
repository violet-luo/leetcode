def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    dic = collections.defaultdict(int) # key为(a + b)之和，value为出现频次
    cnt = 0

    for a in nums1:
        for b in nums2:
            dic[a + b] += 1 # 如果dict中没有key sum, 返回默认频次0
    
    for c in nums3:
        for d in nums4:
            cnt += dic[-(c + d)] # 如果sum出现在AB之和中，累加频次，否则加默认频次0
    
    return cnt
    
###

def fourSumCount(self, A, B, C, D):
    dic = {} # key为(a + b)之和，value为出现频次
    cnt = 0
    
    for a in A:
        for b in B:
            total = a + b
            dic[total] = dic.get(total, 0) + 1 # 如果dict中没有key sum, 返回默认频次0
    
    for c in C:
        for d in D:
            total = c + d
            cnt += dic.get(-total, 0) # 如果sum出现在AB之和中，累加频次，否则加默认频次0
    return cnt
