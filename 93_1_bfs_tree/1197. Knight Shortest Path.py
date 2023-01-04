DIRECTIONS = [
    (-2,-1), (-2,1), (-1,2), (1,2),
    (2,1), (2,-1), (1,-2), (-1,-2)
]

class Solution:
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        # 与200不同
        # 记录从起点到(x,y)的最短距离，(x,y) -> shortest distance from start
        # 在python中，可以使用tuple存储横纵坐标，存入dict
        cell_to_dis_dict = {(source.x, source.y): 0}
        visited = set()

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y): #走到终点
                return cell_to_dis_dict[(x,y)]
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.is_invalid(next_x, next_y, grid):
                    continue
                # 如果之前已经到达过此点，不可能通过再次BFS此点找到最短路，还会造成死循环
                # 这边是类似number of islands里的visited判断
                if (next_x, next_y) in cell_to_dis_dict:
                    continue
                queue.append((next_x, next_y))
                # 与200不同
                cell_to_dis_dict[(next_x, next_y)] = cell_to_dis_dict[(x,y)] + 1
        # 不能达到，返回-1
        return -1

    def is_invalid(self, x, y, grid):
        n, m = len(grid), len(grid[0]) #宽，高
        # 1. 越界
        if x < 0 or x >= n or y < 0 or y >= m:
            return True
        # 2. 碰到1即障碍物，返回false
        return grid[x][y]
