def findNumber(self, array):
    counter = collections.Counter(array) 
    res = 0
    max_count = 0

    for num, count in counter.items():
        if count > max_count:
            max_count = count
            res = num
        elif count == max_count and num < res:
            res = num

    return res
