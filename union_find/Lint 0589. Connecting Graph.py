class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.num_of_set = 0

    def add(self, x):
        if x in self.father:
            return
        # 初始化点的父亲为 None, 点所在集合大小1，集合数量增加1
        self.father[x] = None
        self.size_of_set[x] = 1
        self.num_of_set += 1

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
            self.num_of_set -= 1
            self.size_of_set[root_y] += self.size_of_set[root_x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_num_of_set(self):
        return self.num_of_set 

    def get_size_of_set(self):
        return self.size_of_set[self.find(x)]
