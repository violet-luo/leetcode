def minimumTotal(self, triangle):
    return self.dfs(triangle, 0, 0, {})
    
# 函数返回从 x, y 出发，走到最底层的最短路径值
# visited 中 key 为二元组 (x, y)
# visited 中 value 为从 x, y 走到最底层的最短路径值
def dfs(self, triangle, x, y, visited):
    if x == len(triangle): # x走到底
        return 0
        
    if (x, y) in visited:
        return visited[(x, y)]

    left = self.dfs(triangle, x + 1, y, visited)
    right = self.dfs(triangle, x + 1, y + 1, visited)
    
    visited[(x, y)] = min(left, right) + triangle[x][y]
    return visited[(x, y)]
