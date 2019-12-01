# coding = utf-8


class UnionFind:
    def __init__(self, groups):
        self.groups = groups  # 获得边集合
        self.points = []
        for group in groups:
            self.points += list(group)
        self.points = set(self.points)  # 获得点集合
        self.parent = {}  # 父结点
        self.rootDict = {}  # 记录每个不相交集合下的顶点个数
        for point in self.points:  # 初始化不相交集合的数据结构
            self.rootDict[point] = 1
            self.parent[point] = point

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)
        p = self.rootDict[u]
        q = self.rootDict[v]
        if p >= q:  # 父结点下顶点个数更多的作为新父结点
            self.parent[v] = u
            self.rootDict.pop(v)  # 将顶点从集合中取出并加入对应集合
            self.rootDict[u] = p + q
        else:
            self.parent[u] = v
            self.rootDict.pop(u)
            self.rootDict[v] = p + q

    def find(self, x):
        if x in self.rootDict.keys():
            return x
        else:
            return self.find(self.parent[x])  # 压缩路径,即遍历路径上的每个节点直接指向根节点

    def create_tree(self):
        for group in self.groups:
            if len(group) < 2:
                continue
            else:
                for i in range(0, len(group) - 1):
                    if self.find(group[i]) != self.find(group[i + 1]):  # 归并在同一组却父结点不同的集合
                        self.union(group[i], group[i + 1])

    def print_tree(self):
        rs = {}
        for point in self.points:
            root = self.find(point)
            rs.setdefault(root, [])
            rs[root] += [point]
        for key in rs.keys():
            print(rs[key])

if __name__ == "__main__":
    pairLst = [('b', 'd'), ('e', 'g'), ('a', 'c'), ('h', 'i'), ('a', 'b'),
               ('a', 'b'), ('e', 'f'), ('b', 'c'), 'j']
    uf = UnionFind(pairLst)
    uf.create_tree()
    uf.print_tree()



