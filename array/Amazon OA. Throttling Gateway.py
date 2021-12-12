def droppedRequests(num, requestTime):
    res = 0
    for i in range(num):
        if i>2 and requestTime[i] == requestTime[i-3]:
            res += 1
        elif i>19 and requestTime[i] - requestTime[i-20] < 10:
            res += 1
        elif i > 59 and requestTime[i-60] < 60:
            res += 1
    return res
