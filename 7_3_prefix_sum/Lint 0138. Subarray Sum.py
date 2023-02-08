def subarraySum(self, nums): # [-3, 1, 2, -3, 4]
    result = []

    hash = {0: -1}
    sum = 0 

    for i, num in enumerate(nums): 
        sum += num # -3, 

        # 前缀和曾经出现，即这个区间的和为初始的0
        if sum in hash:
            result.append(hash[sum] + 1) # [0,2]
            result.append(i)
            break #第一次到0，就return
        # 前缀和第一次出现，存入hash
        else:
            hash[sum] = i # {0:-1, -3:0, -2:1}

    return result
