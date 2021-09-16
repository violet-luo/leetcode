DIRECTIONS = [(-2,-1), (-2,1),(-1,2),(1,2),
              (2,1),(2,-1),(1,-2),(-1,-2)]

class Solution:
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x,y = queue.popleft()
            if (x,y) == (destination.x, destination.y):
                return distance[(x,y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x,y)] + 1
                queue.append((next_x, next_y))
        return -1

    def is_valid(self, x, y, grid):
        n,m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return not grid[x][y]
