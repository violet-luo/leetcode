def kthFactor(n, k):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(n // i)
            k -= 1
        if k == 0:
            return i
    if res[-1] ** 2 == n: # 处理完全平方数
        res.pop()
    if k > len(res): # (5,3) returns -1
        return -1
    else:
        return res[-k]
