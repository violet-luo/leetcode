def majorityNumber(self, nums):
    majority_ele = None
    counter = 1 #从1起步是因为1第一次进去会被-1

    for num in nums:
        if num == majority_ele:
            counter += 1
        else:
            # 对冲两个数的出现次数
            counter -= 1
            # 2出现次数比1多
            if counter == 0: # 也可以不缩进，但是会慢一点
                majority_ele = num
                counter = 1
    
    return majority_ele
