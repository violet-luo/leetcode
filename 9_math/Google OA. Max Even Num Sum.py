def max_even_num_sum(N):
    if N % 2 == 1:
        return []
    
    total = 0
    k = 1

    while total < N:
        total = k * (k + 1) 
        k += 1

    diff = total - N

    res = []
    for i in range(1,k):
        res.append(2*i)
    if diff in res:
        res.remove(diff)
    return res
