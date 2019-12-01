# coding = utf-8

from math import sqrt
"""
正确的方法
"""


class Point:
    """
    定义点
    """
    def __init__(self, name='', x=0, y=0, population=0, shortest=float("inf")):
        self.name = name
        self.x = x
        self.y = y
        self.population = population
        self.shortest = shortest


class Pair:
    """
    定义边
    """
    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
        self.distance = sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)
        self.used = False
        self.dp = self.distance

    def __str__(self):
        return "{}（{}）、{}（{}）之间的距离为{}".format(self.point1.name, self.point1.population, self.point2.name, self.point2.population, self.distance)


def prim(points, pairs):
    """
    使用prim方法生成最小生成树
    """
    temp_points = [points[0]]
    # 如果有点未被加入继续执行
    while temp_points.__len__() < points.__len__():
        temp_pairs = []
        for pair in pairs:  # 寻找未被使用且可以使点Q集增加的边
            if pair.used is False:
                if pair.point1 in temp_points or pair.point2 in temp_points:
                    if pair.point1 in temp_points and pair.point2 in temp_points:
                        pass
                    else:
                        temp_pairs.append(pair)
        # 选取符合条件最小的边
        min_pair = min(temp_pairs, key=lambda element: element.distance)
        # 标记边已被使用
        for pair in pairs:
            if pair == min_pair:
                pair.used = True
        # 加入点集Q
        if min_pair.point1 not in temp_points:
            temp_points.append(min_pair.point1)
        if min_pair.point2 not in temp_points:
            temp_points.append(min_pair.point2)
    return pairs


if __name__ == "__main__":
    max_rate = 0  # 最大的比例
    # 初始化
    start = Point('A', 1, 1, 20, 0)
    end = Point('C', 2, 2, 40)
    queue = [start, Point('B', 1, 2, 30), end]
    pointLst = []
    pairLst = []  # 由点生成无向图
    for index1 in range(0, queue.__len__()):
        for index2 in range(index1, queue.__len__()):
            if queue[index1] != queue[index2]:
                pairLst.append(Pair(queue[index1], queue[index2]))
    mst = prim(queue, pairLst)  # 生成最小生成树
    dpPointLst = []  # 辅助列表以求点u到点v的单元最大距离
    mst_length = 0  # 最小生成树的总长度
    for index in range(0, queue.__len__()):  # 做n次循环，相当于第一题求最大能力，以辅助下面求解最大比例
        pointLst.clear()
        for item in queue:
            dpPointLst.append(item)
        while dpPointLst.__len__() != 0:
            point_u = min(dpPointLst, key=lambda element: element.shortest)  # 优先队列选取具有最小shortest的点
            # 优先队列将点移除前将结果保存
            pointLst.append(point_u)
            dpPointLst.remove(point_u)
            for ele in mst:  # 寻找与u结点相邻接的点而产生的边
                if point_u.name == ele.point1.name:
                    for point in dpPointLst:  # 找到点v
                        if point.name == ele.point2.name:
                            point_v = point
                    if point_u.shortest < point_v.shortest and ele.distance < point_v.shortest:  # 做松弛（变形）操作
                        point_v.shortest = max(point_u.shortest, ele.distance)
        for item1 in pairLst:
            if item1.point1.name == pointLst[0].name:
                for item2 in pointLst:
                    if item1.point2.name == item2.name:
                        item1.dp = item2.shortest
        queue[0].shortest, queue[1].shortest = float("inf"), 0
        for index3 in range(0, queue.__len__() - 1):
            queue[index3], queue[index3 + 1] = queue[index3 + 1], queue[index3]
    # 求最小生成树的长度
    for pair1 in mst:
        if pair1.used:
            mst_length += pair1.distance
    # 枚举每条边以求最大比率
    for item3 in mst:
        if item3.used:  # 如果边在最小生成树中
            rate1 = (item3.point1.population + item3.point2.population) / (mst_length - item3.distance)
            max_rate = max(max_rate, rate1)
        else:  # 如果边不在最小生成树中
            rate2 = (item3.point1.population + item3.point2.population) / (mst_length - item3.dp)
            max_rate = max(max_rate, rate2)
    for pair2 in pairLst:
        print(pair2)
    print("A/B最大为{}".format(max_rate), end="")
