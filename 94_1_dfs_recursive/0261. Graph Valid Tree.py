from collections import defaultdict
def validTree(self, n:, edges):
    # 边数 = 结点数- 1
    num_of_edge = len(edges)
    if num_of_edge != n - 1:
        return False
    
    neighbors = defaultdict(list)
    for x, y in edges:
        neighbors[x].append(y)
        neighbors[y].append(x)

    visited = set()

    def dfs(node): 
        visited.add(node)
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)
    return len(visited) == n
