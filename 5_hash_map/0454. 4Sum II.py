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
