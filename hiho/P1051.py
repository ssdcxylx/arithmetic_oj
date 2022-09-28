# -*- coding:utf-8 -*-


def main():
    t = int(raw_input())
    while t > 0:
        (n, m) = (int(x) for x in raw_input().split())
        lst = raw_input().split()
        lst = list(map(int, lst))
        lst.insert(0, 0)
        lst.append(100)
        if m >= n:
            print 100
        else:
            max_num = 0
            for i in range(0, len(lst) - m - 1):
                if lst[i + m + 1] - lst[i] - 1 > max_num:
                    max_num = lst[i + m + 1] - lst[i] - 1
            print max_num
        t = t - 1


if __name__ == '__main__':
    main()
