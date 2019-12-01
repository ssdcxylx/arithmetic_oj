# -*- coding: utf-8 -*-


def main():
    (n, m) = (int(x) for x in raw_input().split())
    need = [0 for i in range(0, n)]
    value = [0 for i in range(0, n)]
    for i in range(0, n):
        (need[i], value[i]) = (int(x) for x in raw_input().split())
    p = [0 for i in range(0, m+1)]
    for i in range(0, n):
        for j in range(m, need[i]-1, -1):
            p[j] = max(p[j], p[j - need[i]] + value[i])
    print p[m]


if __name__ == '__main__':
    main()