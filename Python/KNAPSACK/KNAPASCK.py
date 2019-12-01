# coding = utf-8


class Goods:

    def __init__(self, name=None, volume=0, value=0):
        self.name = name
        self.volume = volume
        self.value = value

    def get_name(self):
        return self.name

    def get_volume(self):
        return self.volume

    def get_value(self):
        return self.value


def knapasck(lst, all):
    """
    利用动态规划求解背包问题
    :param lst:
    :param all:
    :return:
    """
    chart = [[0 for col in range(all + 1)]
             for row in range(lst.__len__() + 1)]  # 初始化结果矩阵，并将其值全部置为0

    chart_flag = [[[] for col in range(all + 1)]
                  for row in range(lst.__len__() + 1)]  # 初始化标志矩阵，并将其值全部置为[]

    for row in range(lst.__len__() + 1):
        for col in range(all + 1):
            if 0 == row or 0 == col:
                chart[row][col] = 0
            elif col < lst[row - 1].get_volume():
                chart[row][col] = chart[row - 1][col]
                chart_flag[row][col] = chart_flag[row - 1][col]
            elif row > 0 and col >= lst[row - 1].get_volume():
                chart[row][col] = max(chart[row - 1][col], chart[row - 1][col - lst[row - 1].get_volume()] + lst[row - 1].get_value())
                if chart[row][col] == chart[row - 1][col]:
                    chart_flag[row][col] = chart_flag[row - 1][col]
                else:
                    chart_flag[row][col] = chart_flag[row - 1][col - lst[row - 1].get_volume()] + [lst[row - 1].get_name()]
    return chart, chart_flag


if __name__ == "__main__":
    goods_lst = [
        Goods('a', 2, 3),
        Goods('b', 3, 4),
        Goods('c', 4, 5),
        Goods('d', 5, 7)]
    knapasck_chart, knapasck_flag = knapasck(goods_lst, all=9)
    # 显示计算列表和标记列表
    print('结果矩阵如下：')
    for i in knapasck_chart:
        print(i)
    print("标志矩阵如下：")
    for j in knapasck_flag:
        print(j)
