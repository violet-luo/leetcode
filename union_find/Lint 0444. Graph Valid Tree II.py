class Solution:
    def __init__(self):
        self.edge_num = 0
        self.vertex_num = 0
        self.tag = 1
        self.f = {}

    def find(self, x):
        if self.f[x] == x:
            return x
        root = x
        while self.f[root] != root:
            root = self.f[root]
        while x != root:
            tmp = self.f[x]
            self.f[x] = root
            x = tmp
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.f[root_x] = root_y
        else:
            self.tag = 0

    def addEdge(self, a, b):
        if a not in self.f:
            self.f[a] = a
            self.vertex_num += 1
        if b not in self.f:
            self.f[b] = b
            self.vertex_num += 1
        self.edge_num += 1
        self.union(a, b)

    def isValidTree(self):
        if self.edge_num + 1 == self.vertex_num and self.tag == 1:
            return True
        else:
            return False
