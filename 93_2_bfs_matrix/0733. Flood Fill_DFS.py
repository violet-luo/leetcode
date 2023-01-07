def floodFill(image, sr, sc, color):
    n, m = len(image), len(image[0])
    visited = set()
    old_color = image[sr][sc]

    def dfs(x, y):            
        image[x][y] = color
        visited.add((x,y))
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            x_, y_ = x + dx, y + dy
            if 0 <= x_ < n and 0 <= y_ < m and (x_, y_) not in visited and image[x_][y_] == old_color: # 而不是image[x_][y_] != color
                dfs(x_, y_)

    dfs(sr, sc) 
    return image

###

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
