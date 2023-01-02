def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1): #-1 因为最后一个元素之后没有元素比较
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
