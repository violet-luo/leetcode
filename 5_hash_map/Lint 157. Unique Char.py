def isUnique(self, str):
    dic = {}

    for char in str:
        if char in dic:
            return False
        else:
            dic[char] = 1
    
    return True

def isUnique(self, str):
    if len(str) > len(set(str)):
        return False
    else: 
        return True
    
def isUnique(self, str):
    hash = set()

    for char in str:
        if char in hash:
            return False
        else:
            hash.add(char)
    
    return True
