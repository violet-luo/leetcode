DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    
    def wallsAndGates(self, A):
        if not A or not A[0]:
            return A
        
        queue = collections.deque([])
        visited = set()
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    # 这题和number of islands不同处是不在这里做BFS
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if self.is_invalid(A, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                A[next_x][next_y] = A[x][y] + 1
        return A
                
                    
    def is_invalid(self, A, next_x, next_y, visited):
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
