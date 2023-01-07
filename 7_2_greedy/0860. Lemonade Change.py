def lemonadeChange(self, bills):
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1
        if bill == 10:
            if five == 0:
                return False
            ten += 1
            five -= 1
        if bill == 20:
            # 1. 10 + 5
            if ten > 0:
                if five == 0:
                    return False
                ten -= 1
                five -= 1
            # 2. 5 + 5 + 5
            else:
                if five < 3:
                    return False
                five -= 3

    return True
