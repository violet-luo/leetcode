def floodFill(self, image, sr, sc, color):
    n, m = len(image), len(image[0])
    old_color = image[sr][sc]
    visited = set()

    def dfs(x, y):
        if x >= n or x < 0 or y >= m or y < 0: return # 这个条件要在第一个，不然会index out of range
        if image[x][y] != old_color: return 
        if (x,y) in visited: return
        image[x][y] = color
        visited.add((x,y))
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            dfs(x+dx, y+dy)

    dfs(sr, sc) 
    return image
