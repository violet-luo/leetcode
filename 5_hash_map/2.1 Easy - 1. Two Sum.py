def twoSum(self, numbers, target):
    # key: value, value: index
    hash = {}

    for i in range(len(numbers)):
        if target - numbers[i] in hash:
            # return the first pair of indices
            return [hash[target - numbers[i]], i] 
        else:
            hash[numbers[i]] = i

    return [-1, -1]
