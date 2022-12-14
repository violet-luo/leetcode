"""
Bruteforce

Runtime: 132 ms, faster than 32.13% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""

def countNegatives(grid):
        count = 0
        for i in range(len(grid)-1, -1,-1):
            for j in range(len(grid[0])-1,-1, -1):
                if grid[i][j]<0:
                    count +=1
        return(count)



"""
Binary Search

Runtime: 116 ms, faster than 98.05% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""

def countNegatives(grid):
    def bin(row):
        start, end = 0, len(row)
        while start<end:
            mid = start +(end -start) // 2
            if row[mid]<0:
                end = mid
            else:
                start = mid+1
        return len(row)- start

    count = 0
    for row in grid:
        count += bin(row)
    return(count)
