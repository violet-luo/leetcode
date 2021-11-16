class Solution:
    def hasPath(self, maze, start, destination): 
        if not maze: 
            return False 
        n, m = len(maze), len(maze[0])

        queue = collections.deque([(start[0], start[1])])
        visited = set()
        while queue:
            x, y = queue.popleft()
            # 从起点一直做BFS联通，直到停止
            visited.add((x, y))
            if (x, y) == (destination[0], destination[1]):
                return True
        
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: #右左下上
                x_, y_ = x, y #这里不能写成标准的next_x, next_y，不然会越界
                # 与number of islands不同的是，如果是valid继续，invalid才停下
                while self.is_valid(maze, x_ + dx, y_ + dy):
                    x_, y_ = x_ + dx, y_ + dy
                # 直到invalid撞墙，将撞墙的前一格加入queue
                if maze[x_][y_] == 0 and (x_, y_) not in visited:
                    queue.append((x_, y_))
        
        return False 
                    

    def is_valid(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
