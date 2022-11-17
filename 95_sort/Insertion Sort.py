def insertionSort(arr): 
    for i in range(1, len(arr)): #从第二个元素开始sort
        cur_val = arr[i]
        while i > 0 and cur_val < arr[i - 1] : #左边的元素小于被交换的元素 #i > 0防止与队尾元素交换
            arr[i] = arr[i - 1] # [1,3,4,2]->[1,3,4,4]->[1,3,3,4]->[1,2,3,4]
            i -= 1
        arr[i] = cur_val
