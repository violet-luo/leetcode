## LC
class UnionFind:
    def __init__(self):
        self.parent = defaultdict()
        self.count = 0

    def add(self, r, c, m, n):
        x = r * n + c
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

        # union with neighbor
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nxt_r, nxt_c = r + dr, c + dc
            if 0 <= nxt_r < m and 0 <= nxt_c < n:
                y = nxt_r * n + nxt_c
                if y in self.parent:
                    self.union(x, y)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def numIslands2(self, m, n, positions):
        uf = UnionFind()
        res = [0] * len(positions)
        for i, (r, c) in enumerate(positions):
            uf.add(r, c, m, n)
            res[i] = uf.count

        return res
    
## Lint 
def numIslands2(self, n, m, operators):
    if not operators:
        return []

    uf = UnionFind()
    island = set() # 记录变成陆地的格子
    res = []

    for operator in operators:
        x, y = operator.x, operator.y
        # 当前坐标陆地，无效
        if (x, y) in island:
            res.append(uf.get_num_of_set())
            continue
        
        # 开辟新的陆地
        island.add((x, y))
        uf.add((x, y))

        # 合并邻居
        for dx, dy in DIRECTIONS:
            x_ = x + dx
            y_ = y + dy
            if self.is_valid(x_, y_, n, m) and (x_, y_) in island:
                uf.merge((x_, y_), (x, y))
            
        res.append(uf.get_num_of_set())
        
    return res
