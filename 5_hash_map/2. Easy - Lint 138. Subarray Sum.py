def subarraySum(self, nums):
    result = []

    hash = {0: -1} #value, index
    sum = 0 

    for i, num in enumerate(nums): 
        sum += num # 累加前缀和

        # 前缀和曾经出现，即这个区间的和为初始的0
        if sum in hash:
            result.append(hash[sum] + 1) #初始index为-1
            result.append(i)
            break #第一次到0，就return
        # 前缀和第一次出现，存入hash
        else:
            hash[sum] = i #sum, index

    return result
