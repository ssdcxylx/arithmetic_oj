# coding=utf-8
"""
made by XuTangjian
"""

import random
from Util import Sort as MySort
from math import sqrt
import operator


class Point:
    """
    二维坐标下的点
    """
    name = ''
    x = 0
    y = 0  # 初始化值为0

    def __init__(self, name, x, y):
        """
        构造方法
        :param name: 点的名称
        :param x: 点的x坐标
        :param y: 点的y坐标
        """
        self.name = name
        self.x = x
        self.y = y

    def __lt__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self < other
        """
        if self.x < other.x or (self.x == other.x and self.y < other.y):
            return True
        else:
            return False

    def __le__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self <= other
        """
        if self.x < other.x or (self.x == other.x and self.y <= other.y):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self > other
        """
        if self.x > other.x or (self.x == other.x and self.y > other.y):
            return True
        else:
            return False

    def __ge__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self >= other
        """
        if self.x > other.x or (self.x == other.x and self.y >= other.y):
            return True
        else:
            return False

    def __eq__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self = other
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        对对象进行x坐标比较，对于x坐标相同的点，再对y坐标进行比较
        self != other
        """
        if self.x == other.x and self.y == other.y:
            return False
        else:
            return True

    def __str__(self):
        """
        将对象以自定义的字符串形式返回，类似于Java的toSting()方法
        :return: 对象的字符串形式
        """
        return "点{}：({},{})".format(self.name, self.x, self.y)


class Pair:
    """
    点对
    """
    p1 = Point('', 0, 0)
    p2 = Point('', 0, 0)  # 初始值为空和0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_instance(self):
        """
        获得点对之间的距离
        :return: 点对之间的距离
        """
        return distance(self.p1, self.p2)

    def __str__(self):
        return "[({},{}),({},{})]".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def nearest_dot(lst):
    length = lst.__len__()
    left_lst = lst[:length//2]
    right_lst = lst[length//2:]
    mid_x = (left_lst[-1].x + right_lst[0].x)/2  # 对点集合进行分割，分而治之

    if left_lst.__len__() > 2:  # 左侧部分最近点对，如果长度大于2，继续分割
        l_min = nearest_dot(left_lst)
    else:
        l_min = left_lst

    if right_lst.__len__() > 2:  # 右侧部分最近点对，如果长度大于2，继续分割
        r_min = nearest_dot(right_lst)
    else:
        r_min = right_lst

    if l_min.__len__() == 2:
        pair = Pair(l_min[0], l_min[1])
        d1 = pair.get_instance()
    else:
        d1 = float("inf")  # 无穷大

    if r_min.__len__() == 2:
        pair = Pair(r_min[0], r_min[1])
        d2 = pair.get_instance()
    else:
        d2 = float("inf")

    d = min(d1, d2)

    mid_min = []

    for pointL in left_lst:
        if mid_x - pointL.x <= d:  # 如果左侧部分与中间线的距离小于或等于d
            for pointR in right_lst:
                if abs(pointL.x - pointR.x) <= d and abs(pointL.y - pointR.y) <= d:  # 如果右侧部分点在pointL点的正方形d的范围内
                    if distance(pointL, pointR) <= d:
                        mid_min.append([pointL, pointR])

    if mid_min:  # 如果d3<d1,d2，最短距离为d3
        dic = []
        for mid_point in mid_min:
            dic.append([distance(mid_point[0], mid_point[1]), mid_point])
        dic.sort(key=lambda x: x[0])  # 以列表中的的列表第二项为排序项
        return list(dic[0])[1]  # 取最小的一项
    elif d1 < d2:
        if l_min.__len__() == 2:
            return l_min
        else:
            return
    else:
        if r_min.__len__() == 2:
            return r_min
        else:
            return


def distance(point1, point2):
    """
    两点间的距离
    """
    if operator.__ne__(point1, point2):
        return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    else:
        return float("inf")  # 如果为两个相同的点则返回无穷大


if __name__ == "__main__":

    pointLst = []
    for i in range(10):
        pointLst.append(Point(i, random.randint(0, 99), random.randint(0, 99)))  # 随机添加十个点
    # 将点集合继续排序，先对x坐标进行排序，对于x坐标相同的点，再对y坐标进行排序
    MySort.Sort.quick_sort(pointLst, 0, pointLst.__len__() - 1)
    # MySort.Sort.shell_sort(pointLst, pointLst.__len__())  # 希尔排序

    # pointLst.sort(key=lambda point: (point.x, point.y))  # python内置函数非常强大
    for point in pointLst:
        print("{}{},{}{},".format("{", point.x, point.y, "}"), end="")  # 格式化输出点集合

    print()
    my_pair = Pair(nearest_dot(pointLst)[0], nearest_dot(pointLst)[1])
    print("最短边为：{}，长度为：{}".format(my_pair.__str__(), distance(nearest_dot(pointLst)[0], nearest_dot(pointLst)[1])))



