def selection_sort(arr):
    n = len(arr)
    for i in range(n-1): #n-1 因为不需要比较最后一个元素
        min_val_idx = i # 被比较的元素
        for j in range(i+1, n):
            if arr[j] < arr[min_val_idx]:
                min_val_idx = j
        arr[min_val_idx], arr[i] = arr[i], arr[min_val_idx]
        
    return arr
