def minCost(self, colors: str, neededTime: List[int]) -> int:
    min_cost = 0
    n = len(colors)
    i = 0

    while i < n:
        color = colors[i]
        max_cost = 0
        total = 0      
    
        while i < n and colors[i] == color:
            max_cost = max(max_cost, neededTime[i])
            total += neededTime[i]
            i += 1
    
        min_cost += total - max_cost
    
    return min_cost
