# [3, 0, 6, 1, 5]
def h_index(citations):
    citations.sort() #[0, 1, 3, 5, 6]
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n - i:
            return i - 1
    return 0
