DIR = [(0,1), (0,-1), (1,0), (-1,0)]
class Solution:
    def exist(self, board, word):
        if not word:
            return True 
        n, m = len(board), len(board[0])   
        visited = set() #假如visited防止回头 #abc找abcb
        
        for i in range(n):
            for j in range(m):
                if self.dfs(i, j, word, 0, n, m, visited, board):
                    return True 
                        
        return False 
        
    def dfs(self, x, y, word, index, n, m, visited, board):
        if index >= len(word):
            return True 
            
        if x >= n or x < 0 or y >= m or y < 0:
            return False 
            
        if (x,y) in visited:
            return False 
        
        if board[x][y] != word[index]:    
            return False 
            
        visited.add( (x,y) )  
        
        for dx, dy in DIR:
            if self.dfs(x + dx, y + dy, word, index + 1, n, m, visited, board):
                return True 
                
        visited.remove( (x,y) ) #回溯，走到(3,0)的E后退到(2，0)的C，往(0, -1)方向走      
        return False
