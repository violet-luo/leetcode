def highFive(self, items):
    dic = collections.defaultdict(list)
    import heapq 
    for item in items:
        heapq.heappush(dic[item[0]], item[1])
        if len(dic[item[0]]) > 5:
            heapq.heappop(dic[item[0]])
    
    res = []
    for id, score_list in dic.items():
        avg = sum(score_list) // len(score_list)
        res.append([id, avg])
    
    res.sort(key = lambda x: x[0])
    return res
