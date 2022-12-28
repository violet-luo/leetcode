def hasPath(self, maze, start, destination):
    visited = set((start[0], start[1]))

    def dfs(x, y):
        if [x, y] == destination:
            return True
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x_, y_ = x + dx, y + dy
            while 0 <= x_ < len(maze) and 0 <= y_ < len(maze[0]) and maze[x_][y_] == 0:
                x_, y_ = x_ + dx, y_ + dy

            # 遇到墙，往回退一格
            x_, y_ = x_ - dx, y_ - dy
            if (x_, y_) not in visited: 
                visited.add((x_, y_))
                if dfs(x_, y_):
                    return True
        return False # 一定要加！不然没有出口

    return dfs(start[0], start[1])
