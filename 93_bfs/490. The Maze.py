DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def hasPath(self, maze, start, destination): 
        if not maze: 
            return False 
            n, m = len(maze), len(maze[0])
        
        queue = collections.deque([(start[0], start[1])]) # 起点坐标
        visited = set()
        
        while queue:
            x, y = queue.popleft()
            # 从起点一直做BFS联通，直到停止
            visited.add((x, y))
            if (x, y) == (destination[0], destination[1]): # 终点坐标
                return True
        
            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy
                # 与number of islands不同的是，如果是valid继续，invalid才停下
                if self.is_valid(maze, next_x, next_y): 
                    continue
                # 直到invalid撞墙，将撞墙的前一格加入queue
                if maze[x][y] == 0 and (x, y) not in visited:
                    queue.append((x, y))
        
        return False 
                    
    def is_valid(self, maze, x, y):
        n, m = len(maze), len(maze[0])
        if 0 <= x < n and 0 < y < m and maze[x][y] == 0:
            return True
        return False
