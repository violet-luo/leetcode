def floodFill(image, sr, sc, color):
    n, m = len(image), len(image[0])
    old_color = image[sr][sc]
    if old_color == color: # 不加会TLE
        return image
    queue = collections.deque([(sr,sc)])

    while queue:
        x, y = queue.popleft()
        image[x][y] = color
        for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < n and 0 <= new_y < m and image[new_x][new_y] == old_color:
                image[new_x][new_y] = color
                queue.append((new_x, new_y))
    
    return image
