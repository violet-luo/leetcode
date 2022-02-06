def reverse_array(arr):
    dict = {}
    if len(arr) < 1:
        return 
        
    for num in arr:
        if str(num) == str(num)[::-1]:
            dict[str(num)] = 1
        elif str(num) not in dict and str(num)[::-1] not in dict:
            dict[str(num)] = 1
        elif str(num) in dict:
            dict[str(num)] += 1
            if dict[str(num)] > 2:
                dict[str(num)] -= 1  
        elif str(num)[::-1] in dict:
            dict[str(num)[::-1]] += 1
            if dict[str(num)[::-1]] > 2:
                dict[str(num)[::-1]] -= 1
              
    result = 0
    for d in dict:
        result += dict[d]
    
    return result
