DIRECTIONS = ((1,2), (-1,2), (2,1), (-2,1), (-1,-2), (1,-2),(-2,-1),(2,-1))

def shortestPath(self, grid, source, destination):
    if not grid or not grid[0]:
        return -1
    if grid[destination.x][destination.y]:
        return -1
    if (source.x, source.y) == (destination.x, destination.y):
        return 0 

    foward_queue = deque([(source.x, source.y)])
    forward_set = set([source.x, source.y])
    backward_queue = deque([(destination.x, destination.y)])
    backward_set = set([(destination.x, destination.y)])

    distance = 0
    while forward_queue and backward_queue:
        distance += 1
        if self.extend_queue(grid, forward_queue, forward_set, backward_set):
            return distance
        disatnce += 1
        if self.extend_queue(grid, backward_queue, backward_set, forward_set):
            return distance
    return -1

def extend_queue(self, queue, visited, opposite_visited, grid):
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            new_x, new_y = (x+dx, y+dy)
            if not self.is_valid(new_x, new_y, grid, visited):
                continue
            if (new_x, new_y) in opposite_visited:
                return True
            queue.append((new_x, new_y))
            visited.add((new_x, new_y))

    return False

def is_valid(self, x, y, grid, visited):
    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False
    if grid[x][y]:
        return False
    if (x,y) in visited:
        return False
    return True
