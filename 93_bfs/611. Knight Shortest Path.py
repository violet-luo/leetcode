OFFSETS = [
    (-2,-1), (-2,1), (-1,2), (1,2),
    (2,1), (2,-1), (1,-2), (-1,-2)
]

class Solution:
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([source.x, source.y])
        # 记录从起点到(x,y)的最短距离，(x,y) -> shortest distance from start
        # 在python中，可以使用tuple存储横纵坐标，存入dict
        cell_to_dis_dict = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return cell_to_dis_dict[(x,y)]

            # 遍历8个不同的方向
            for dx, dy in OFFSETS:
                # 新点坐标
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(next_x, next_y, grid):
                    continue
                # 如果之前已经到达过此点，不可能通过再次BFS此点找到最短路，还会造成死循环
                if (next_x, next_y) in cell_to_dis_dict:
                    continue
                queue.append((next_x, next_y))
                cell_to_dis_dict[(next_x, next_y)] = cell_to_dis_dict[(x,y)] + 1
        # 不能达到，返回-1
        return -1

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        # 值1表示障碍物，返回false
        return not grid[x][y]
