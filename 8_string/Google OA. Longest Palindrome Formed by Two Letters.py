# ['oo', 'oo', 'oo', 'kk']
def longestPalindrome(arr):
    dict = {}
    result_len = 0
    max_odd = 0
   
    for ele in arr:
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1
   
    for e in dict:
        if e[::-1] in dict:
            if e != e[::-1]: # ok, ko case
                result_len += min(dict[e], dict[e[::-1]]) * 2
            elif dict[e] % 2 != 0: # oo, oo case
                if dict[e] > max_odd: # oo出现基数次
                    max_odd = dict[e]
                else:
                    result_len += (dict[e]-1) * 2
            else:
                result_len += dict[e] * 2 # kk长度
    
    result_len += max_odd * 2 # oo长度
    return result_len
