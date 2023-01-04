def reverseArray(arr):
    dict = {}
    if len(arr) < 1:
        return
        
    for num in arr:
        str_num = str(num)     
        if str_num not in dict:
            dict[str_num] = 1     
        elif str_num in dict and str_num[::-1] not in dict:
            dict[str_num[::-1]] = 1            
       
    return sum(dict.values()) 
