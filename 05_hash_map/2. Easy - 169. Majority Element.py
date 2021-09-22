def majorityNumber(self, nums):
    storedNum = None
    counter = 1 #从1起步是因为1第一次进去会被-1

    for num in nums:
        if num == storedNum:
            counter += 1
        else:
            # 对冲两个数的出现次数
            counter -= 1
            # 2出现次数比1多
            if counter == 0:
                storedNum = num
                counter = 1

    return storedNum
