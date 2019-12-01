# coding = utf-8
"""
made by XuTangjian
"""

import random

def merge_sort(lst):
    """
    该排序方法名为四路归并排序
    将集合划分为四部分
    :param lst: 待划分的集合
    :return: 返回排序好的部分集合
    """
    length = lst.__len__()
    if length < 2:  # 如果集合长度小于2，则直接返回该集合
        return lst
    while length < 4:  # 如果集合长度大于2小于4，则补足4个
        lst.append(float("inf"))
        length += 1
    # 划分数组
    lst_group1 = merge_sort(lst[:length // 4])
    lst_group2 = merge_sort(lst[length // 4: length // 2])
    lst_group3 = merge_sort(lst[-(length // 2): -(length // 4)])  # 负数代表从右往左
    lst_group4 = merge_sort(lst[-(length // 4):])

    return merge(lst_group1, lst_group2, lst_group3, lst_group4)


def merge(lst_group1, lst_group2, lst_group3, lst_group4):
    """
    将集合进行归并
    """
    g1, g2, g3, g4 = 0, 0, 0, 0  # 记录各集合排序个数
    result = []  # 结果集合
    while g1 < lst_group1.__len__() or g2 < lst_group2.__len__()\
            or g3 < lst_group3.__len__() or g4 < lst_group4.__len__():  # 如果还有未排序的元素
        if lst_group1[g1] == float("inf") and lst_group2[g2] == float("inf")\
                and lst_group3[g3] == float("inf") and lst_group4[g4] == float("inf"):  # 如果每个集合最后一个都为无穷大，则说明排序合并完成
            break
        # 如果元素最大，则加入合并后的集合
        elif lst_group1[g1] <= lst_group2[g2] and lst_group1[g1] <= lst_group3[g3] and lst_group1[g1] <= lst_group4[g4]:
            result.append(lst_group1[g1])
            # 如果已经排序到集合最后一个，然后再往集合中添加一个无穷大
            if g1 == lst_group1.__len__()-1:
                lst_group1.append(float("inf"))
            g1 += 1
        elif lst_group2[g2] <= lst_group1[g1] and lst_group2[g2] <= lst_group3[g3] and lst_group2[g2] <= lst_group4[g4]:
            result.append(lst_group2[g2])
            if g2 == lst_group2.__len__()-1:
                lst_group2.append(float("inf"))
            g2 += 1
        elif lst_group3[g3] <= lst_group1[g1] and lst_group3[g3] < lst_group2[g2] and lst_group3[g3] <= lst_group4[g4]:
            result.append(lst_group3[g3])
            if g3 == lst_group3.__len__() - 1:
                lst_group3.append(float("inf"))
            g3 += 1
        elif lst_group4[g4] <= lst_group1[g1] and lst_group4[g4] <= lst_group2[g2] and lst_group4[g4] <= lst_group3[g3]:
            result.append(lst_group4[g4])
            if g4 == lst_group4.__len__() - 1:
                lst_group4.append(float("inf"))
            g4 += 1
    return result

if __name__ == "__main__":
    lst = []
    for i in range(10):
        lst.append(random.randint(0, 100))
    print("排序前的列表：{}".format(lst))
    print("排序后的列表：{}".format(merge_sort(lst)))
