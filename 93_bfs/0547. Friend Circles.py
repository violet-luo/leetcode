def findCircleNum(self, isConnected: List[List[int]]) -> int:
    if not isConnected:
        return 0

    visited = set()
    res = 0
    # 遍历每个省，如果这个省还没访问过 就从这个省开始做一遍bfs
    for i in range(len(isConnected)):
        if i not in visited:
            visited.add(i)
            self.bfs(i, isConnected, visited)
            res += 1
    return res

def bfs(self, node, isConnected, visited):
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
