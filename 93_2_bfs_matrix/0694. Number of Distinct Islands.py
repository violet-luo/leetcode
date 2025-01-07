def numDistinctIslands(self, grid: List[List[int]]) -> int:
  if not grid or not grid[0]:
      return 0

  n, m = len(grid), len(grid[0])
  shapes = set()

  def bfs(i, j):
      q = collections.deque([(i, j)])
      grid[i][j] = 0
      shape = []
      while q:
          x, y = q.popleft()
          for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
              new_x, new_y = x + dx, y + dy
              if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                  grid[new_x][new_y] = 0
                  q.append((new_x, new_y))
                  shape.append((new_x - i, new_y - j))
      return tuple(sorted(shape))

  for i in range(n):
      for j in range(m):
          if grid[i][j] == 1:
              shape = bfs(i, j)
              shapes.add(shape)

return len(shapes)
    
###

def numDistinctIslands(self, grid):
    if not grid or not grid[0]: return 0
    n, m = len(grid), len(grid[0])
    
    queue, seen, res = collections.deque(), set(), 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                path = " "
                queue.append((i, j))
                grid[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                            queue.append((new_x, new_y))
                            grid[new_x][new_y] = 0
                            path += str(new_x - i) + str(new_y - j) # 不同的地方
                if path not in seen:
                    res += 1
                    seen.add(path)
    return res
  
###
  
  def numberofDistinctIslands(self, grid):
    if not grid or not grid[0]: return 0
    n, m = len(grid), len(grid[0])

    def bfs(x,y):
        queue = collections.deque([(i, j)])
        visited = set([(i, j)])
        shape = ''

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = 0
                    visited.add((new_x, new_y))
                    shape += str(new_x - i) + str(new_y - j) # 与200不同的地方

        return shape

    count = 0
    shapes = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] == 0
                shape = bfs(i, j)
                if shape in shapes:
                    continue
                count += 1
                shapes.add(shape)

    return count
