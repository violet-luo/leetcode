def exist(n, m, matrix, letters):
    res = ['No'] * len(letters)
    for i in range(len(letters)):
        for j in range(n):
            for k in range(m):
                letter = letters[i]
                if dfs(j, k, letter, 0, n, m, matrix):
                        res[i] = 'Yes'
    return res

def dfs(x, y, letter, index, n, m, matrix):
    if index >= len(letter):
        return True
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if matrix[x][y] != letter[index]:
        return False
    if dfs(x+1, y, letter, index+1, n, m, matrix):
        return True
    if dfs(x-1, y, letter, index+1, n, m, matrix):
        return True
    if dfs(x, y+1, letter, index+1, n, m, matrix):
        return True
    if dfs(x, y-1, letter, index+1, n, m, matrix):
        return True
      
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
       
