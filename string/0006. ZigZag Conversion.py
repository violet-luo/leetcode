"""

Runtime: 40 ms, faster than 99.72% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.1 MB, less than 23.73% of Python3 online submissions for ZigZag Conversion.

"""

def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows -1:
            step = -1
        index += step

    return ''.join(L)
