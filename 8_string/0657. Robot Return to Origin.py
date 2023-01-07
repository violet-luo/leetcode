def judgeCircle(moves):
    dic = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    x, y = 0, 0

    for move in moves:
        x += dic[move][0]
        y += dic[move][1]

    return (x, y) == (0,0)

###

def judgeCircle(self, moves):
    x = y = 0
    for move in moves:
        if move == 'U': y -= 1
        elif move == 'D': y += 1
        elif move == 'L': x -= 1
        elif move == 'R': x += 1

    return x == y == 0
