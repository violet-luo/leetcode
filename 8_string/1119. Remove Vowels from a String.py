def removeVowels(self, s):
    vowels = ['a','e','i','o','u']
    res = ''
    
    for c in s:
        if c.lower() not in vowels:
            res += c
    return res
