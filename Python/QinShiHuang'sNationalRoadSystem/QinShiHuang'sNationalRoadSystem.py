# coding = utf-8

from math import sqrt
"""
错误的方法
"""


class Point:
    """
    定义点
    """
    def __init__(self, name='', x=0, y=0, population=0):
        self.name = name
        self.x = x
        self.y = y
        self.population = population


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
        return "{}到{}的距离为{}".format(self.point1.name, self.point2.name, self.distance)


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
    # 初始化
    max_rate = 0
    start = Point('A', 1, 1, 20)
    end = Point('C', 2, 2, 40)
    pointLst = [start, Point('B', 1, 2, 30), end]
    pairLst = []  # 由点生成无向图
    for index1 in range(0, pointLst.__len__()):
        for index2 in range(index1, pointLst.__len__()):
            if pointLst[index1] != pointLst[index2]:
                pairLst.append(Pair(pointLst[index1], pointLst[index2]))
    mst = prim(pointLst, pairLst)
    temp_mst1, mst_length = [], 0  # 保存最小生成树和最小生成树长度
    for pair1 in mst:
        if pair1.used:
            mst_length += pair1.distance
    for pair1 in mst:
        temp_mst1.clear()
        for pair2 in mst:
            if pair2.used:
                temp_mst1.append(pair2)
        if pair1.used:
            rate1 = (pair1.point1.population + pair1.point2.population) / (mst_length - pair1.distance)
            max_rate = max(max_rate, rate1)
        else:
            mst2_length = 0
            max_pair = max(temp_mst1, key=lambda element: element.distance)
            for pair2 in mst:
                if pair2.point1.name == pair1.point1.name and pair2.point2.name == pair1.point2.name:
                    pair2.used = True
                    temp_mst1.append(pair2)
            for pair3 in temp_mst1:
                if pair3.point1.name == max_pair.point1.name and pair3.point2.name == max_pair.point2.name:
                    pair3.used = False
            max_pair1 = max(temp_mst1, key=lambda element: element.distance)
            for pair2 in temp_mst1:
                if pair2.used:
                    mst2_length += pair2.distance
            if (mst2_length - max_pair1.distance) != 0:
                rate1 = (max_pair1.point1.population + max_pair1.point2.population) / (mst2_length - max_pair1.distance)
            else:
                rate1 = 0
            max_rate = max(max_rate, rate1)
    print(max_rate)


