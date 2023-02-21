def shortestDistance(self, maze, start, destination):
    start = (start[0], start[1])
    destination = (destination[0], destination[1])
    n, m = len(maze), len(maze[0])
    queue = collections.deque([(start)])
    visited = {start: 0}

    def get_next_point(point, visited):
        points = {}
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = point
            count = -1
            while 0 <= x < n and 0 <= y < m and maze[x][y] == 0:
                x, y = x + dx, y + dy
                count += 1
            points[(x - dx, y - dy)] = visited[point] + count
        
        return points

    while queue:
        point = queue.popleft()
        next_points = get_next_point(point, visited)
        for next_point in next_points:
            if next_point in visited:
                if next_points[next_point] < visited[next_point]:
                    visited[next_point] = next_points[next_point]
            else:
                queue.append(next_point)
                visited[next_point] = next_points[next_point]
        
    if destination in visited:
        return visited[destination]
    return -1
