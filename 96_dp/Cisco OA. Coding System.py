def coding_system(s):
    return helper(s, 0)

def helper(s, i):
    # base case: if loop till the end of str
    if i == len(s) - 1:
        return 1
    if i == len(s) - 2:
        if (s[i] == '2' and int(s[i+1]) <= 5) or (s[i] == '1'):
            return 2
        else:
            return 1
    
    #recursion logic
    # 1(2456)+12(456)
    if (s[i] == '2' and int(s[i+1]) <= 5) or (s[i] == '1'):
        return helper(s, i+1)+ helper(s, i+2)
    else:
        return helper(s, i+1)
