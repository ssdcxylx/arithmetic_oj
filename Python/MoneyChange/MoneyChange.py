# coding = utf-8


ALL_METHOD = []  # 定义全局变量保存所有解决办法


class Method:

    info = ''
    length = 0

    def __init__(self, info, length=0):
        self.info = info
        self.length = length


def money_change(lst, method_lst, money=0):
    """
    兑换零钱
    :param lst:零钱面值
    :param method_lst: 解决办法列表
    :param money:金额
    :return:
    """
    temp = []  # 用于储存当前计算的结果
    global ALL_METHOD  # 声明为全局变量
    if money > 0 and len(lst) > 0:
        temp.extend(method_lst)
        if len(lst) > 1:
            money_change(lst[0: len(lst) - 1], temp, money)
        if money >= lst[len(lst) - 1]:
            method_lst.append(lst[len(lst) - 1])
            temp.clear()
            temp.extend(method_lst)
            money_change(lst[0: len(lst)], temp, money - lst[len(lst) - 1])
    elif money <= 0:
        ALL_METHOD.append(Method(method_lst, len(method_lst)))


# def money_change(lst, money=0):
#     """
#     兑换零钱
#     :param lst:零钱面值
#     :param money:金额
#     :return:
#     """
#     num = [[0 for col in range(money + 1)]
#              for row in range(lst.__len__())]  # 初始化结果矩阵，并将其值全部置为1
#     for row in range(0, lst.__len__()):
#         num[row][0] = 1  # 设定第一列为1，表示金额为0时，仍有一种兑换方法
#
#     for row in range(1, lst.__len__()):
#         for col in range(money + 1):
#             if col < lst[row]:
#                 num[row][col] = num[row - 1][col]
#             else:
#                 num[row][col] = num[row - 1][col] + num[row][col - lst[row]]
#     return num


if __name__ == "__main__":
    coins = [2, 3, 5, 6]
    num_lst = []
    min_num = 0
    # for element in money_change(coins, 10):
    #     print(element)

    money_change(coins, [], 10)
    for element in ALL_METHOD:
        print(element.info)
    ALL_METHOD.sort(key=lambda method: method.length)  # 排序
    for element in ALL_METHOD:
        if element.length == ALL_METHOD[0].length:
            print("兑换的最小个数为{}，组成为：{}".format(element.length, sorted(element.info)))


