def fourSumCount(self, A, B, C, D):
    # key为(a + b)之和，value为出现频次
    dictionary = {}
    
    for a in A:
        for b in B:
            total = a + b
            # 如果dict中没有key sum, 返回默认频次0
            dictionary[total] = dictionary.get(total, 0) + 1
    
    cnt = 0
    for c in C:
        for d in D:
            total = c + d
            # 如果sum出现在AB之和中，累加频次，否则加默认频次0
            cnt += dictionary.get(-total, 0)
    return cnt
