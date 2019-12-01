# coding = utf-8

import random

__author__ = "XuTangjian"


def get_frequency(lst, index):
    """
    找到数值位置后，向两边进行查找
    :param lst: 待查找的集合
    :param index: 数值位置
    :return:
    """
    num = lst[index]
    count = 1
    left_index, right_index = index - 1, index + 1
    while left_index > 0:
        if lst[left_index] == num:
            count += 1
            left_index -= 1
        else:
            break
    while right_index < lst.__len__():
        if lst[right_index] == num:
            count += 1
            right_index += 1
        else:
            break
    return count


def find_num(lst, num):
    """
    利用二分查找法，查找已排序数组内该数值的位置
    :param lst: 待查找的集合
    :param num: 需要寻找的数字
    :return:
    """
    length = lst.__len__()
    count = 0
    if length > 0:
        mid = lst[length // 2]
        if mid == num:
            index = length//2
            count = get_frequency(lst, index)
            print("{}出现的次数为：{}".format(num, count))
        elif mid > num:
            find_num(lst[:length // 2], num)
        elif mid < num:
            find_num(lst[length // 2 + 1:], num)
    else:
        print("{}出现的次数为：{}".format(num, count))


if __name__ == "__main__":
    arr = []
    for arr_index in range(0, 15):
        arr.append(random.randint(0, 15))
    for i in arr:
        print(i, end=" ")
    print()
    arr.sort()  # 内置排序函数
    for i in arr:
        print(i, end=" ")
    randint = random.randint(0, 15)
    print()
    find_num(arr, randint)
