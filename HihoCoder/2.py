# -*- coding -*-
import sys


def main():
    t = input()
    while t > 0:
        lst = sys.stdin.readline().split()[0]
        lst = list(map(int, lst))
        for i in range(0, len(lst)):
            a = sum(lst[0:i])
            b = sum(lst[i:])
            if a == b:
                print 'YES'
                break
            else:
                if i == len(lst)-1:
                    print 'NO'
        t -= 1


if __name__ == '__main__':
    main()