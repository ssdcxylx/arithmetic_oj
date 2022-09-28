# -*- coding: utf-8 -*-


def main():
    t = input()
    n = t
    while t > 0:
        lst1 = raw_input().split(' ')
        lst2 = raw_input().split(' ')
        m1 = lst1[0]
        # hihocoder python版本太低无法执行
        # d1 = int(lst1[1][0:len(lst1)-1])
        d1 = lst1[1]
        d1 = d1[0:len(d1)-1]
        d1 = int(d1)
        y1 = int(lst1[2])
        m2 = lst2[0]
        d2 = lst2[1]
        d2 = d2[0:len(d2) - 1]
        d2 = int(d2)
        y2 = int(lst2[2])
        if m1 == 'January' or (m1 == 'February' and d1 <= 29):
            y1 -= 1
        if m2 == 'January' or (m2 == 'February' and d2 < 29):
            y2 -= 1
        # 快速计算闰年
        num = y2 // 400 - y1 // 400 + y2 // 4 - y1 // 4 - (y2 // 100 - y1 // 100)
        print 'Case #{0}: {1}'.format(n - t + 1, num)
        t -= 1


if __name__ == '__main__':
    main()