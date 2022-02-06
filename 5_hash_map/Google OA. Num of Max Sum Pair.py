def max_sum_pair(A):
    hash = {}
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] not in hash:
                hash[A[i] + A[j]] = [i,j]
            elif i not in hash[A[i] + A[j]] and j not in hash[A[i] + A[j]]:
                hash[A[i] + A[j]].append(i)
                hash[A[i] + A[j]].append(j)
                
    max_len = 0
    for i in hash:
        if len(hash[i]) > max_len:
            max_len = len(hash[i])
    return max_len//2
