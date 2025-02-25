def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    fresh_oranges = 0
    rotten_queue = collections.deque()
    
    # 第一步：找到所有腐烂的橙子，并计算新鲜橙子的数量
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                rotten_queue.append((i, j))
    
    # 边界情况：如果没有新鲜橙子，直接返回 0
    if fresh_oranges == 0:
        return 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 第二步：用 BFS 模拟腐烂过程
    minutes = 0
    while rotten_queue:
        minutes += 1
        for _ in range(len(rotten_queue)):
            x, y = rotten_queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # 变成腐烂橙子
                    fresh_oranges -= 1  # 新鲜橙子数量减少
                    rotten_queue.append((nx, ny))  # 腐烂的橙子加入队列
    
    # 第三步：检查是否还有剩余的新鲜橙子
    return minutes - 1 if fresh_oranges == 0 else -1
