# coding = utf-8

import queue


class Pair:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.visited = 0


class Point:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color

if __name__ == "__main__":
    flag = True  # 标志是否为二分图
    # 初始化点
    A = Point('A')
    B = Point('B')
    C = Point('C')
    D = Point('D')
    E = Point('E')
    a = Point('a')
    b = Point('b')
    c = Point('c')
    d = Point('d')
    # 初始化图
    graph = [Pair(A, a), Pair(B, a), Pair(B, b), Pair(D, b), Pair(C, c), Pair(C, d), Pair(E, a), Pair(E, d),
             Pair(a, A), Pair(a, B), Pair(b, B), Pair(b, D), Pair(c, C), Pair(d, C), Pair(a, E), Pair(d, E)]
    # 初始化状态
    my_queue = [A]
    pointQueue = queue.deque(my_queue)
    A.color = 'red'
    point = pointQueue.pop()
    # 如果队列不为空
    while point is not None:
        points = []
        # 寻找相邻顶点
        for element in graph:
            if element.visited == 0 and point.name == element.point1.name:
                element.visited = 1
                points.append(element.point2)
                # 如果相邻顶点还未被染色，则染上其相邻顶点相反的颜色
                if element.point2.color is None:
                    if element.point1.color == 'red':
                        element.point2.color = 'green'
                    else:
                        element.point2.color = 'red'
                elif element.point2.color != element.point1.color:
                    break
                else:
                    print("不是二分图")
                    flag = False
        points = set(points)  # 确保点唯一
        # 加入队列
        for element in points:
            pointQueue.append(element)
        # 出队列
        if pointQueue.__len__() > 0:
            point = pointQueue.pop()
        else:
            point = None
            if flag:
                print("是二分图")











