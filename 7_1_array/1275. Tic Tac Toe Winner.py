from itertools import permutations
def tictactoe(self, moves):
    A = moves[::2]
    B = moves[1::2]
    for a,b,c in itertools.permutations(A, 3):
        if (b[1] - a[1])*(c[0] - a[0]) == (c[1] - a[1])*(b[0] - a[0]): #斜率
            return "A"
    for a,b,c in itertools.permutations(B, 3):
        if (b[1] - a[1])*(c[0] - a[0]) == (c[1] - a[1])*(b[0] - a[0]):
            return "B"
    
    if len(A) + len(B) == 9:
        return "Draw"
    else:
        return "Pending"
