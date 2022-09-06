def stringCount(self, str):
    if not str:
        return 0

    zero_count, res = 0, 0
    for i in str: # 而不是for i in range(len(str))
        if i == '0':
            zero_count += 1
        else:
            res += (1 + zero_count) * zero_count // 2;
            zero_count = 0

    #如果最后1位1后还有0, e.g. 0100100
    if zero_count != 0:
        res += (1 + zero_count) * zero_count // 2;

    return res
