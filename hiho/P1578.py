# -*- coding -*-
import sys


def main():
    while True:
        try:
            (n, m) = (int(x) for x in raw_input().split())
            p = list(map(int, raw_input().split()))
            q = list(map(int, raw_input().split()))
            q = q[1:]
            a, b = 0, 0
            min = sys.maxint
            for i in range(n-m+1):
                if i not in q:
                    j = i
                    k = 0
                    while j < n:
                        if j not in q:
                            k += 1
                        if k == m:
                            for l in range(i+1, j+1):
                                if l not in q:
                                    if min > p[i] + p[l]:
                                        min = p[i] + p[l]
                                        a = i
                                        b = l
                        j == n
                        j += 1
            print a, b
        except EOFError:
            break
        except ValueError:
            break


if __name__ == '__main__':
    main()