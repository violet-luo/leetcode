def isStrobogrammatic(self, num):
    map = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    i, j = 0, len(num)-1
    while i<=j:
        if not num[i] in map or map[num[i]] != num[j]:
            return False
        i, j = i+1, j-1
    return True
