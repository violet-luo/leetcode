class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if not word:
            return True 
        m,n = len(board), len(board[0])   
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, m, n, visited, i, j):
                    return True 
                        
        return False 
        
    def dfs(self, board, word, index, m, n, visited, x, y):
        if x >= m or x < 0 or y >= n or y < 0:
            return False 
        if (x,y) in visited:
            return False  
        # 这条要写在word[index] != board[x][y]前，不然会index out of range
        if index >= len(word):
            return True
        if word[index] != board[x][y]:    
            return False 
        
        visited.add((x,y))  
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x, next_y = x + dx, y + dy
            
            if self.dfs(board, word, index + 1, m, n, visited, next_x, next_y):
                return True 
        # 如果没match上，字母可以继续用        
        visited.remove( (x,y) )     
        return False
      
# Cisco OA 变种
def exist(n, m, matrix, letters):
    res = ['No'] * len(letters)
    for i in range(len(letters)):
        for j in range(n):
            for k in range(m):
                letter = letters[i]
                if dfs(j, k, letter, 0, n, m, matrix, ''):
                        res[i] = 'Yes'
    return res

def dfs(x, y, letter, index, n, m, matrix, direction):
    if index >= len(letter):
        return True
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if matrix[x][y] != letter[index]:
        return False
    if dfs(x+1, y, letter, index+1, n, m, matrix, 'right') and direction in ['', 'right']:
        return True
    if dfs(x-1, y, letter, index+1, n, m, matrix, 'left') and direction in ['', 'left']:
        return True
    if dfs(x, y+1, letter, index+1, n, m, matrix, 'up') and direction in ['', 'up']:
        return True
    if dfs(x, y-1, letter, index+1, n, m, matrix, 'down') and direction in ['', 'down']:
        return True
       
