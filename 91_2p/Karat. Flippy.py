def reversi(board):
    maxLen, idx, l = 0, 0, 0
    
    for r in range(len(board)):
        if board[r] == 'O': #找到第一个空
            continue

        while l < r:
            if board[l] == 'X' and board[r] == ' ':
                curLen = (r - l - 1) # 中间O的数量
                if curLen > maxLen:
                    maxLen = curLen
                    idx = r

            if board[l] == ' ' and board[r] == 'X':
                curLen = (r - l - 1)
                if curLen > maxLen:
                    maxLen = curLen
                    idx = l

            l += 1 #将l带到R
    
    return [idx, maxLen] if idx or maxLen else [None, None]
