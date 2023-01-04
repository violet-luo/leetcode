def kthSmallest(self, matrix, k): # [[1,5,9],[10,11,13],[12,13,15]]
    n = len(matrix) #注：题目中这个矩阵是n*n的，所以长宽都是n

    # 取出第一列候选人
    # matrix[i][0]是具体的值，后面的(i,0)是在记录候选人在矩阵中的位置，方便每次右移添加下一个候选人
    # [[1,0,0],[10,1,0],[12,2,0]]
    pq = [(matrix[i][0], i, 0) for i in range(n)] 
    

    impor heapq
    heapq.heapify(pq)

    for i in range(k - 1): #一共弹k次：这里k-1次，return的时候1次
        num, x, y = heapq.heappop(pq) #弹出候选人里最小一个，即[1,0,0]
        if y != n - 1: #如果这一行还没被弹完
            # 加入这一行的下一个候选人, [[5,0,1],[12,2,0],[10,1,0]], [[9,0,2],[12,2,0],[10,1,0]]
            heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
    
    return heapq.heappop(pq)[0]
