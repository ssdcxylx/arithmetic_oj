# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 22:56
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : CharacterCombination.py


def cc(lst, pre=''):
    if len(lst) == 1:
        print(lst[0]+pre)
    for x in lst:
        temp = lst.copy()
        temp.remove(x)
        cc(temp, pre=pre+x)


if __name__ == '__main__':
    cc(['a', 'b', 'c'])