#!/usr/bin/python
# -*- encoding: utf-8 -*-

import threading

# 地图（字符串，用于描绘地图）
strings = [
    '#####################',
    '#...................#',
    '#...................#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#S........#........E#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#.........#.........#',
    '#...................#',
    '#...................#',
    '#####################'
]
# 地图（列表，用于实际计算）
my_map = []

# 线程锁
threadLock = threading.RLock()
# 线程列表
threads = []

# 查找过的位置
searched = []

# 起点线程当前查找位置
threadOriginPos = None
# 终点线程当前查找位置
threadEndPos = None


class NodeElement:
    """
    开放列表与关闭列表的结点
    """

    def __init__(self, parent, x, y, distance):
        self.parent = parent
        self.x = x
        self.y = y
        self.distance = distance

    def __str__(self):
        return "x:{0},y:{1}".format(self.x, self.y)


class AStar(threading.Thread):
    """
    A*算法线程实现类
    """

    def __init__(self, start_x, start_y, end_x, end_y, originType):
        # 线程初始化
        threading.Thread.__init__(self)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        self.originType = originType

        self.width = my_map[0].__len__()
        self.height = my_map.__len__()

        self.open = []  # 开放列表
        self.close = []  # 关闭列表
        self.path = []  # 路径

    # 查找路径
    def run(self):
        # 构建起点
        start_element = NodeElement(None, self.start_x, self.start_y, 0.0)
        while True:
            # 扩展F值最小的节点
            self.extend_round(start_element)
            # 如果开放列表为空，则不存在路径
            if not self.open:
                return
            # 获得F值最小的节点
            index, start_element = self.get_min_f()
            if self.originType:
                global threadOriginPos
                threadOriginPos = start_element
            else:
                global threadEndPos
                threadEndPos = start_element
            # 找到路径，并返回
            if self.reach_target():
                self.end_x = start_element.x
                self.end_y = start_element.y
                self.make_path(start_element)
                self.get_searched()
                # 标记已搜索区域
                mark_searched(searched)
                # 标记路径
                mark_path(self.path)
                # 标记起点和终点
                # mark_start_end(self.start_x, self.start_y, self.end_x, self.end_y)
                return
            # 把此节点压入关闭列表，并从开放列表删除
            self.close.append(start_element)
            del self.open[index]

    def extend_round(self, current_element):
        # 八个方向
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0),
                      (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for x, y in directions:
            next_x, next_y = x + current_element.x, y + current_element.y
            if self.is_valid(next_x, next_y, next_x - x, next_y - y):
                # 构造新的节点
                node = NodeElement(
                    current_element,
                    next_x,
                    next_y,
                    current_element.distance +
                    self.get_cost(
                        current_element.x,
                        current_element.y,
                        next_x,
                        next_y))
                # 新节点在关闭列表则跳过
                if not self.node_in_close(node):
                    index = self.node_in_open(node)
                    if index != -1:
                        # 新节点在开放列表
                        if self.open[index].distance > node.distance:
                            # 如果路径更短则选择更短的路径
                            self.open[index].parent = current_element
                            self.open[index].distance = node.distance
                    else:
                        self.open.append(node)

    def is_valid(self, x, y, pre_x, pre_y):
        # 判断下一个位置是否有效
        if x <= 0 or x >= self.height or y <= 0 or y >= self.width:
            return False
        if pre_x - x == 1 and pre_y - y == 1:
            if my_map[pre_x -
                      1][pre_y] == '#' or my_map[pre_x][pre_y -
                                                        1] == '#':
                return False
        if pre_x - x == -1 and pre_y - y == 1:
            if my_map[pre_x +
                      1][pre_y] == '#' or my_map[pre_x][pre_y -
                                                        1] == '#':
                return False
        if pre_x - x == -1 and pre_y - y == -1:
            if my_map[pre_x +
                      1][pre_y] == '#' or my_map[pre_x][pre_y +
                                                        1] == '#':
                return False
        if pre_x - x == 1 and pre_y - y == -1:
            if my_map[pre_x -
                      1][pre_y] == '#' or my_map[pre_x][pre_y +
                                                        1] == '#':
                return False
        return my_map[x][y] != '#'

    def get_cost(self, x1, y1, x2, y2):
        """
        走直线的代价为10，走斜线得代价为14
        """
        if x1 == x2 or y1 == y2:
            return 10
        return 14

    def node_in_close(self, node):
        for element in self.close:
            if node.x == element.x and node.y == element.y:
                return True
        return False

    def node_in_open(self, node):
        for index, element in enumerate(self.open):
            if node.x == element.x and node.y == element.y:
                return index
        return -1

    def get_min_f(self):
        # 初始化最优值
        best = None
        best_value = 99999999
        best_index = -1
        for index, element in enumerate(self.open):
            value = self.get_distance(element)  # 获取F值
            if value <= best_value:
                best = element
                best_value = value
                best_index = index
        return best_index, best

    def get_distance(self, element):
        # F = G + H
        # G 为已经移动耗费， H为不考虑障碍理论移动耗费
        return element.distance + \
            (abs(self.end_x - element.x) + abs(self.end_y - element.y)) * 10

    def reach_target(self):
        global threadEndPos
        global threadOriginPos
        print("Origin:{0},End:{1}".format(threadOriginPos, threadEndPos))
        # 到达目标
        if threadOriginPos is not None and threadEndPos is None:
            return threadOriginPos.x == self.end_x and threadOriginPos.y == self.end_y
        if threadEndPos is not None and threadOriginPos is None:
            return threadEndPos.x == self.end_x and threadEndPos.y == self.end_y
        if threadOriginPos is not None and threadEndPos is not None:
            return threadOriginPos.x == threadEndPos.x and threadOriginPos.y == threadEndPos.y

    def make_path(self, element):
        # 从结束点回溯到开始点生成路径
        while element:
            self.path.append((element.x, element.y))
            element = element.parent

    def get_searched(self):
        for element in self.open:
            searched.append((element.x, element.y))
        for element in self.close:
            searched.append((element.x, element.y))


def find_path():
    global threadEndPos
    global threadEndPos
    start_x, start_y = get_start_xy()
    end_x, end_y = get_end_xy()
    thread_origin = AStar(start_x, start_y, end_x, end_y, True)
    thread_end = AStar(end_x, end_y, start_x, start_y, False)
    thread_origin.start()
    thread_end.start()
    # 添加线程至线程列表
    threads.append(thread_origin)
    threads.append(thread_end)
    # 等待所有线程结束
    for thread in threads:
        thread.join()
    print_my_map()
    print("Origin:{0},End:{1}".format(threadOriginPos, threadEndPos))


def get_start_xy():
    return get_symbol_xy('S')


def get_end_xy():
    return get_symbol_xy('E')


def get_symbol_xy(s):
    for x, line in enumerate(my_map):
        try:
            y = line.index(s)
        except BaseException:
            continue
        else:
            break
    return x, y


def mark_searched(lst):
    mark_symbol(lst, ' ')


def mark_path(lst):
    mark_symbol(lst, '*')


def mark_symbol(lst, s):
    for x, y in lst:
        if my_map[x][y] == ' ' and s == '*':
            my_map[x][y] = s
        if my_map[x][y] == '.':
            my_map[x][y] = s
        if my_map[x][y] == '*':
            pass


def mark_start_end(start_x, start_y, end_x, end_y):
    my_map[start_x][start_y] = 'S'
    my_map[end_x][end_y] = 'E'


def strings_to_my_map():
    for line in strings:
        my_map.append(list(line))


def print_my_map():
    for line in my_map:
        print(''.join(line))


if __name__ == "__main__":
    strings_to_my_map()
    find_path()
