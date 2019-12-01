# -*- coding:utf-8 -*-
import math
import sys


def main():
    lst1 = list(map(int, raw_input().split()))
    lst2 = raw_input()
    lst3 = [0 for x in range(3)]
    lst1.sort()
    red = 0
    yellow = 0
    blue = 0
    max = 0
    num = 0
    for x in lst2:
        if x == 'R':
            red += 1
        elif x == 'Y':
            yellow += 1
        elif x == 'B':
            blue += 1
        num += 1
        if num > max:
            max = num
        lst3[0] = int(math.fabs(red - yellow))
        lst3[1] = int(math.fabs(red - blue))
        lst3[2] = int(math.fabs(yellow - blue))
        lst3.sort()
        if lst3[0] == lst1[0] and lst3[1] == lst1[1] and lst3[2] == lst1[2]:
            red = 0
            yellow = 0
            blue = 0
            num = 0
    print max


if __name__ == '__main__':
    main()