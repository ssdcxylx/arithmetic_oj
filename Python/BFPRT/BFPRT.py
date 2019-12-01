# coding = utf-8
"""
made by XuTangjian
"""

import random
import operator

"""
BFPRT算法，又称中位数的中位数算法，是目前解决TOP-K问题最有效的算法，最坏时间复杂度是O(n)
还有比较排序、计数排序、堆排序、堆选择、遍历所有数据、快速排序等算法
"""


def get_median_medians(lst):
    """
    选择主元，即中位数的中位数
    """
    length = lst.__len__()
    while length >= 5:
        cols = length // 5  # 只保留整数位，其他的舍去，符合BFPRT第一步的思想
        temp = []
        for i in range(0, cols):
            group = sorted(lst[5*i: 5*i+5])  # 将集合切分为长度为5的组
            temp.append(group[2])  # 因为已经是排序好的5个元素的集合，所以第3个位中位数
        lst = temp
        length = lst.__len__()
    lst.sort()
    return lst[length//2]  # 返回中位数的中位数


def partition(lst, pivot_index):
        """
        根据主元将数组分割为两部分
        :param lst: 需要排序的集合
        :param pivot_index: 主元的坐标
        :return:
        """
        pivot_value = lst[pivot_index]
        low = 0
        high = lst.__len__() - 1
        lst[pivot_index], lst[0] = lst[0], lst[pivot_index]  # 将主元放在第一个位置
        while high > low:  # 当low>high时，表示两个位置已经反了，查找交换结束
            # 如果左边坐标值比右边坐标值小而且左边坐标值对应的数据值比主元小，则左边坐标值加1
            while low <= high and operator.le(lst[low], pivot_value):
                low += 1

            # 如果左边坐标值比右边坐标值小而且右边坐标值对应的数据值比主元大，则右边坐标值减一
            while low <= high and operator.gt(lst[high], pivot_value):
                high -= 1

            # 如果满足找到两个不符合左边小于主元值，右边大于主元值，则将两数交换
            if high > low:
                # 两数进行交换，相当于Java的Swap函数
                lst[high], lst[low] = lst[low], lst[high]

        while high > pivot_index and operator.ge(lst[high], pivot_value):  # 将high的坐标值移到其值小于主元
            high -= 1

        if operator.gt(pivot_value, lst[high]):  # 如果主元比high所指的值大，则将两值进行交换，返回high的坐标值，否则返回low的坐标值
            lst[0], lst[high] = lst[high], lst[0]
            return high
        else:
            return 0


def bfprt(lst, k):
    """
    递归执行该函数，如果k小于主元位置则在集合左边，如果k大于主元位置则在右边，如果k等于主元位置则该位置元素为第k小的元素
    :param lst: 需要进行操作的集合
    :param k: top-kd的数值
    :return:
    """
    pivot = get_median_medians(lst)
    pivot_index = lst.index(pivot)
    index = partition(lst, pivot_index)
    if k > index + 1:
        return bfprt(lst[index+1:], k - index - 1)
    elif k == index + 1:
        return lst[index]
    elif k < index + 1:
        return bfprt(lst[0: index], k)


if __name__ == "__main__":
    sort_lst = [3, 1, 7, 0, 8, 4, 2, 6, 9, 5]
    # for i in range(15):
    #     sort_lst.append(random.randint(0, 100))
    #     print(sort_lst[i], end=" ")
    tempLst = []
    for element in sort_lst:
        tempLst.append(element)
    # randint = random.randint(1, 15)
    # print("第{}小的数为{}".format(randint, bfprt(sort_lst, randint)))
    print("列表{}的中位数是{}".format(tempLst,  bfprt(sort_lst, 5)))
    # temp.sort()
    # print(temp)
