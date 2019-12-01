# coding = utf-8
"""
排序类
made by XuTangjian
"""

import operator


class Sort:
    """
    排序工具类
    """

    @staticmethod
    def quick_sort(lst, first=0, last=0):
        """
        快速排序
        :param lst: 需要排序的集合
        :param first: 集合的第一个元素的位置，这里将它作为主元
        :param last: 集合最后一个元素的位置
        :return: null
        """

        if last > first:
            pivot_index = Sort.partition(lst, first, last)  # 找到主元的位置
            # 递归执行
            Sort.quick_sort(lst, first, pivot_index - 1)
            Sort.quick_sort(lst, pivot_index + 1, last)

        return

    @staticmethod
    def partition(lst, first, last):
        """
        根据主元将数组分割为两部分
        :param lst: 需要排序的集合
        :param first: 集合的第一个元素的位置，这里将它作为主元
        :param last: 集合最后一个元素的位置
        :return:
        """
        pivot = lst[first]
        low = first + 1
        high = last
        while high > low:  # 当low>high时，表示两个位置已经反了，查找交换结束
            # 如果左边坐标值比右边坐标值小而且左边坐标值对应的数据值比主元小，则左边坐标值加1
            while low <= high and operator.le(lst[low], pivot):
                low += 1

            # 如果左边坐标值比右边坐标值小而且右边坐标值对应的数据值比主元大，则右边坐标值减一
            while low <= high and operator.gt(lst[high], pivot):
                high -= 1

            # 如果满足找到两个不符合左边小于主元值，右边大于主元值，则将两数交换
            if high > low:
                # 两数进行交换，相当于Java的Swap函数
                lst[high], lst[low] = lst[low], lst[high]

        while high > first and operator.ge(lst[high], pivot):  # 将high的坐标值移到其值小于主元
            high -= 1

        if operator.gt(pivot, lst[high]):  # 如果主元比high所指的值大，则将两值进行交换，返回high的坐标值，否则返回low的坐标值
            lst[first], lst[high] = lst[high], pivot
            return high
        else:
            return first

    @staticmethod
    def shell_sort(lst, length):
        """
        希尔排序
        :param lst: 需要排序的集合
        :param length: 集合长度
        :return:
        """
        step_size = 1
        while step_size < length // 3:  # Knuth提出的步长序列
            step_size = 3 * step_size + 1

        while step_size >= 1:
            for i in range(step_size, length):
                j = i
                tmp = lst[i]
                while j >= step_size and operator.__lt__(lst[j], lst[j - step_size]):
                    lst[j] = lst[j - step_size]
                    lst[j - step_size] = tmp
                    j -= step_size
            step_size //= 3

"""
# 测试
if __name__ == "__main__":
    sortLst = [5, 2, 9, 3, 8, 4, 0, 1, 6, 7]
    Sort.quick_sort(sortLst, 0, len(sortLst)-1)
    # Sort.shell_sort(sortLst, len(sortLst))
    for index in sortLst:
        print(sortLst[index], end=" ")
"""



