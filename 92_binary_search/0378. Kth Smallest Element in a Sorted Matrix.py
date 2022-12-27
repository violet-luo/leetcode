def kthSmallest(self, matrix, k):
    m, n = len(matrix), len(matrix[0])
    start, end = matrix[0][0], matrix[-1][-1]
    while start + 1 < end:
        mid = (start + end) // 2
        count = self.num_of_less_or_equal(matrix, mid)
        if count < k:
            start = mid 
        else:
            end = mid 
    
    if self.num_of_less_or_equal(matrix, start) >= k:
        return start 
    return end  
        
def num_of_less_or_equal(self, matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = m-1, 0
    count = 0
    while i >= 0 and j < n:
        if matrix[i][j] <= target:
            count += i+1 
            j += 1 
        else:
            i -= 1 
    return count
