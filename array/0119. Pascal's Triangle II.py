"""

Runtime: 28 ms, faster than 75.13% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 14 MB, less than 23.30% of Python3 online submissions for Pascal's Triangle II.

"""

def getRow(self, rowIndex: int) -> List[int]:
    res = []

    for i in range(1, rowIndex + 2):
        res.append(1)
        for j in range(i - 2, 0, -1):
            res[j] += res[j-1]

    return res
