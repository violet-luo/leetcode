def romanToInt(self, s):
    roman_to_int = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    
    for i in range(len(s) - 1):
        if roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            res -= roman_to_int[s[i]]
        else:
            res += roman_to_int[s[i]]

    return res + roman_to_int[s[-1]] # 别忘了加最后的一个数字，不能用roman_to_int[i+1]
