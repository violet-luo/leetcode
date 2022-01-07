def isRobotBounded(self, instructions: str) -> bool:
    x, y= 0, 0
    # 方向用向量表示，分别代表，N, E, S, W.
    dirs  = [[0,1], [1, 0], [0, -1], [-1, 0]] 
    
    # 初始方向是北
    i = 0 
    for inst in instructions:
        if inst  == 'G':
            # 沿着当前向量移动
            x, y = x + dirs[i%4][0], y + dirs[i%4][1] 
        elif inst == 'L':
            i -= 1 # 逆时针
        elif inst == 'R':
            i += 1 # 顺时针
    
    return (x == 0 and y == 0) or (i%4 != 0)
