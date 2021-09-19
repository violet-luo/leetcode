def singleNumber(self, nums):
    dic = {}

    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    # items() method is used to return the list with all dictionary keys with values
    for key,val in dic.items():
        if val == 1:
            return key
