def isStrobogrammatic(self, num):
    dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    
    res = ''
    for n in num[::-1]:
        if n not in dic:
            return False 
        
        res += dic[n] 
        
    return res == num
