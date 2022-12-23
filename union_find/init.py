class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x in self.father:
            return
        # 初始化点的父亲为 None
        self.father[x] = None

    def find(self, x):
        # 不断找root的父亲，直到root指向根节点
        root = x
        while self.father[root]:
            root = self.father[root]
        #路径优化
        while x != root:
            original_father = self.father[x]
            self.father[x] = root 
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != rooy_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
