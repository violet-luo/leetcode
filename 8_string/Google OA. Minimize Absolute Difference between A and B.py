def min_ab(N):
    str_N = str(N)
    min_diff = N
    res = 0
    
    if len(str_N) <= 1:
        return 0
    
    for i in range(1,len(str_N)):
        A = str(N)[:i] 
        B = str(N)[i:]
        diff = abs(int(A) - int(B))
        if diff < min_diff:
            min_diff = diff
    
    return min_diff
