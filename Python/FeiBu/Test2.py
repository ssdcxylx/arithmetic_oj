# -*- coding -*-
import sys


def main():
    t = input()
    while t > 0:
        lst = sys.stdin.readline().split()[0]
        lst = list(map(int, lst))
        while 0 in lst:
            lst.remove(0)
        flag = False
        for i in range(1, len(lst)):
            sum1 = sum(lst[0:i])
            sum2 = 0
            for j in range(i, len(lst)):
                sum2 += lst[j]
                if sum2 == sum1:
                    if j == len(lst)-1:
                        flag = True
                    else:
                        sum2 = 0
        if flag:
            print 'YES'
        else:
            print 'NO'
        t -= 1


if __name__ == '__main__':
    main()