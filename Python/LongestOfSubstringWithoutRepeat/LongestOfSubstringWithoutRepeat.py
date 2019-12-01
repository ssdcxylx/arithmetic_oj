# -*- coding: utf-8 -*-
# @Time    : 2019-08-05 22:49
# @Author  : ssdcxy
# @Email   : 18379190862@163.com
# @File    : LongestOfSubstringWithoutRepeat.py


def loswr(s):
    maxlen = 0
    res = ''
    for ch in s:
        if ch not in res:
            res += ch
        else:
            maxlen = max(maxlen, len(res))
            index = res.index(ch)
            res = res[index+1:] + ch
    return max(maxlen, len(res))


if __name__ == '__main__':
    print(loswr("eeydgwdykpv"))