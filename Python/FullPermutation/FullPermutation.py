# coding = utf-8


PERMUTATION_NUM = 0  # 记录全排列的个数


def full_permutation(lst, begin, end):
    """
    递归求解全排列
    :return:
    """
    global PERMUTATION_NUM
    if begin >= end:
        PERMUTATION_NUM = PERMUTATION_NUM + 1
        print(lst)
    else:
        flag = begin
        for index in range(begin, end):
            lst[index], lst[begin] = lst[begin], lst[index]
            full_permutation(lst, begin + 1, end)
            lst[index], lst[begin] = lst[begin], lst[index]


if __name__ == "__main__":
    my_lst = [1, 2, 3, 4, 5]
    full_permutation(my_lst, 0, len(my_lst))
    print("全排列的个数为：{}".format(PERMUTATION_NUM))

