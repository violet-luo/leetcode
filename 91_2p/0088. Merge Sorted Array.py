def mergeSortedArray(A, m, B, n):
    if not A:
        return B
    if not B:
        return A 

    i, j = 0, 0
    res = []

    while i < m and j < n:
        if A[i] <= B[j]: # 不要忘了等号
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    # 这样会变成[1,2,3,[4,5]]
    # if i < m: 
    #     res.append(A[i:])
    # if j < n:
    #     res.append(B[j:])

    while i < m:
        res.append(A[i])
        i += 1
    while j < n:
        res.append(B[j])
        j += 1

    return res
