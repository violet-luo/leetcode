def chessboard(n):    
    return [["BW"[(i+j+n%2+1) % 2] for i in range(n)] for j in range(n)]
