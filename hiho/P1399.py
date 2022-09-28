# -*- coding:utf-8-*-
import sys
import math


# 加速控制台输入
def read_int():
    return list(map(int, sys.stdin.readline().split()))


def read_str():
    return sys.stdin.readline().split()[0]


def main():
    n = read_int()[0]
    lst = read_int()
    cnt = 0
    # 奇偶相消
    for i in range(n):
        if lst[i] % 2 == 0:
            cnt += 1
        else:
            cnt -= 1
    # 加上0.1防止数据异常
    print int(math.fabs(cnt) + 0.1)


if __name__ == '__main__':
    main()