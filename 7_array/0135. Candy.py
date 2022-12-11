def candy(ratings): #[5,7,8,3,4,2,1]
    n = len(ratings)
    left = right = [1] * n

    for i in range(1, n): #[1,2,3,1,2,1,1]
        if ratings[i] > ratings[i - 1]: 
            left[i] = left[i - 1] + 1
    
    count = left[-1] #1
    
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]: 
            right[i] = right[i + 1] + 1
        count += max(left[i], right[i])
    return count
