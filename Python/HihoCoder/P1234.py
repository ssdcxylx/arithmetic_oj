# -*- coding:utf-8 -*-


def main():
    lst = [0]
    for i in range(1, 500):
        x = (lst[i - 1] + 0.5) / 2
        lst.append(x)
    t = input()
    while t > 0:
        k = input()
        if k > 0.5:
            k = 1 - k
        for i in range(0, len(lst)-1):
            if lst[i] < k < lst[i+1]:
                print 4 * (i+1)
            elif k == lst[i] or k == lst[i]:
                print -1
        t -= 1


if __name__ == '__main__':
    main()