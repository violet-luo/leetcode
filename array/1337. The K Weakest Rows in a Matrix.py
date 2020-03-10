"""
Runtime: 92 ms, faster than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.
"""

def kWeakestRows(mat, k):
    s = [[sum(g),i] for i,g in enumerate(mat)]
    r = sorted(s)
    return [r[1] for r in r[:k]]
