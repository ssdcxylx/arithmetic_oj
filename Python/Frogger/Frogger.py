# coding = utf-8

from math import sqrt


class Point:
    """
    定义点
    """
    def __init__(self, name='', x=0, y=0, shortest=float("inf")):
        self.name = name
        self.x = x
        self.y = y
        self.shortest = shortest  # 初始值为无穷大


class Pair:
    """
    定义边
    """
    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
        self.distance = sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)

    def __str__(self):
        return "{}、{}之间的距离为{}".format(self.point1.name, self.point2.name, self.distance)

if __name__ == "__main__":
    # 建立优先队列，顶点的shortest为0，其余点的shortest为∞
    start = Point('A', 0, 0, 0)
    end = Point('E', 3, 0)
    queue = [start, Point('B', 1, 1), Point('C', 1, 2), Point('D', 2, 0), end]
    pointLst = []  # 保存结果
    pairLst = []  # 由点生成无向图
    for index1 in range(0, queue.__len__()):
        for index2 in range(index1, queue.__len__()):
            if queue[index1] != queue[index2]:
                pairLst.append(Pair(queue[index1], queue[index2]))
    while queue.__len__() != 0:  # 优先队列不为空
        point_u = min(queue, key=lambda element: element.shortest)  # 优先队列选取具有最小shortest的点
        # 优先队列将点移除前将结果保存
        pointLst.append(point_u)
        queue.remove(point_u)
        for pair in pairLst:  # 寻找与u结点相邻接的点而产生的边
            if point_u.name == pair.point1.name:
                for point in queue:  # 找到点v
                    if point.name == pair.point2.name:
                        point_v = point
                if point_u.shortest + pair.distance < point_v.shortest:  # 做松弛操作
                    point_v.shortest = point_u.shortest + pair.distance
                # if point_u.shortest < point_v.shortest and pair.distance < point_v.shortest:  # 做松弛（变形）操作
                #     point_v.shortest = max(point_u.shortest, pair.distance)
    for result in pointLst:
        if result.name == end.name:
            end = result
        if result.name == start.name:
            start = result
    for pair in pairLst:
        print(pair)
    print("点{}到点{}需要最小的跳跃能力是{}".format(start.name, end.name, end.shortest))



