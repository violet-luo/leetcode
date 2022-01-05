def minElements(self, arr):
    n = len(arr)
    halfSum = 0
    
    for i in range(n):
        halfSum = halfSum + arr[i]
    halfSum = int(halfSum / 2)
    arr.sort(reverse = True)
    res = 0
    curr_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        res += 1
        if curr_sum > halfSum:
            return res
    return res
