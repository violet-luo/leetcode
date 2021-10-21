import collections
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

def wallsAndGates(A):
    if not A or not A[0]:
        return A
    
    n, m = len(A), len(A[0])
    queue, visited = collections.deque([]), set()
    get_sources(A, queue, visited)
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if is_invalid(A, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))
            A[next_x][next_y] = A[x][y] + 1
    return A
            

def get_sources(A, queue, visited):
    n, m = len(A), len(A[0])
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))
                
                
def is_invalid(A, next_x, next_y, visited):
    n, m = len(A), len(A[0])
    if next_x < 0 or next_x >= n:
        return True
    if next_y < 0 or next_y >= m:
        return True
    if (next_x, next_y) in visited:
        return True
    if A[next_x][next_y] != 2147483647:
        return True
    return False

wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
