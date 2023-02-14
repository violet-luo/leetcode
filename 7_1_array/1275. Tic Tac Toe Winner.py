from itertools import permutations
def tictactoe(self, moves): # [[0,0],[2,0],[1,1],[2,1],[2,2]]
    A = moves[::2]
    B = moves[1::2]

    # [0, 0] [1, 1] [2, 2]
    # [0, 0] [2, 2] [1, 1]
    # [1, 1] [0, 0] [2, 2]
    # [1, 1] [2, 2] [0, 0]
    # [2, 2] [0, 0] [1, 1]
    # [2, 2] [1, 1] [0, 0] 
    for a,b,c in itertools.permutations(A, 3):
        # 三点成线，即两根两点成线的斜率相等
        # (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)
        # # 不用除法，为了防止division by 0
        if (b[1] - a[1])*(c[0] - a[0]) == (c[1] - a[1])*(b[0] - a[0]):
            return "A"
    for a,b,c in itertools.permutations(B, 3):
        if (b[1] - a[1])*(c[0] - a[0]) == (c[1] - a[1])*(b[0] - a[0]):
            return "B"

    if len(A) + len(B) == 9:
        return "Draw"
    else:
        return "Pending"
