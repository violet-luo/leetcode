def findNumber(self, array):
    counter = collections.Counter(array) 
    answer = 0
    count = 0

    for num, count in counter.items():
        if count > max_count:
            max_count = count
            answer = num
        elif count == max_count and num < answer:
            answer = num

    return answer
