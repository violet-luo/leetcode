def minElements(self, arr):
    n = len(arr)
    sum = 0
    res = 0
    
    for i in range(n):
        sum = sum + arr[i]
    half_sum = int(sum / 2)
    arr.sort(reverse = True)
    
    curr_sum = 0 
    for i in range(n):
        curr_sum += arr[i]
        res += 1
        if curr_sum > half_sum:
            return res
    return res
