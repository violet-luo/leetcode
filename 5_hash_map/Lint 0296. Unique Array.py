def getUniqueArray(self, arr):
    unique_arr = []
    dic = {}

    for char in arr:
        if char not in dic:
            unique_arr.append(char)
            dic[char] = 1
    
    return unique_arr
