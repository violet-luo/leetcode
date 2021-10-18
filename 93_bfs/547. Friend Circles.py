import collections

class Solution:
    def beginbfs(self, M):
        n = len(M)
        ans = 0
        visisted = {}
        
        for i in range(n):
            visisted[i] = False
        # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍bfs
        for i in range(n):
            if (visisted[i] == False):
                ans += 1
                q = collections.deque()
                # 标记起点并压入队列
                visisted[i] = True
                q.append(i)
                while (len(q) != 0):
                    # 取出队首
                    now = q.popleft()
                    # 从队首找朋友
                    for j in range(n):
                        # 找到新朋友（之前没访问过的朋友）就标记访问并压入队列
                        if (M[now][j] == 1 and visisted[j] == False):
                            visisted[j] = True
                            q.append(j)
        return ans

    def findCircleNum(self, M):
        ansbfs = self.beginbfs(M)
        return ansbfs
