# [10,8,2,1,9]
def max_sum_pair(A):
    hash = {}
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] not in hash: #{18: [0,1]}
                hash[A[i] + A[j]] = [i,j]
            elif i not in hash[A[i] + A[j]] and j not in hash[A[i] + A[j]]:
                hash[A[i] + A[j]].append(i) #{11: [0,3,2,4]}
                hash[A[i] + A[j]].append(j)
    
    # 找最长的value
    max_len = 0
    for i in hash:
        if len(hash[i]) > max_len:
            max_len = len(hash[i])
    return max_len//2
