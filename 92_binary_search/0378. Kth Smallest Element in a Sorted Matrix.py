def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n, m = len(matrix), len(matrix[0])
    l, h = matrix[0][0], matrix[n-1][m-1] # 矩阵中最小最大的值

    while l + 1 < h:
        mid = (l + h) // 2
        count = self.num_of_less_or_equal(matrix, mid) # 小于或等于 mid 的元素个数
        if count < k:
            l = mid 
        else:
            h = mid 
    
    if self.num_of_less_or_equal(matrix, l) >= k:
        return l 
    
    return h
        
        
def num_of_less_or_equal(self, matrix, target):
    n, m = len(matrix), len(matrix[0])
    i, j = n-1, 0 #从左下角出发
    count = 0
    while i >=0 and j < m:
        if matrix[i][j] <= target: 
            count += i + 1 # 当前列之前的元素i + 这个元素1
            j += 1 
        else:
            i -= 1 # 去上一行
    return count
