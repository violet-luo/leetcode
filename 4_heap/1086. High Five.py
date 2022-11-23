from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def highFive(self, records):
        scores = defaultdict(list)

        for record in records:
            heappush(scores[record.id], record.score)
            if (len(scores[record.id])) > 5:
                heappop(scores[record.id])

        scores_avg = {}
        for id in scores:
            scores_avg[id] = sum(scores[id]) / 5.0
            
        return scores_avg
