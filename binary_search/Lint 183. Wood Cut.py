def woodCut(self, L, k):
    if not L:
        return 0

    # 木头长度至少为1
    start, end = 1, min(max(L), sum(L) // k)

    if end < 1:
        return 0

    while start + 1 < end:
        mid = (start + end) // 2
        if self.get_pieces(L, mid) >= k:
            start = mid
        else:
            end = mid;

    # 要更大的数，从end起看
    if self.get_pieces(L, end) >= k:
        return end
    if self.get_pieces(L, start) >= k:
        return start

    return 0

def get_pieces(self, L, length):
    pieces = 0
    for l in L:
            pieces += l // length
    return pieces 
