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
