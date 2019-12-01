# -*- coding:utf-8 -*-
import sys
maxn = 100000
MAXNUM = 26
INF = int(1e8)

g = [[True for j in range(MAXNUM)] for i in range(MAXNUM)]
f = [0 for _ in range(MAXNUM)]


def read_int():
    return list(map(int, sys.stdin.readline().split()))


def read_str():
    return sys.stdin.readline().split()[0]


def no(ch):
    return ord(ch) - ord('a')


def main():
    n = read_int()[0]
    s = read_str()
    m = read_int()[0]
    for i in range(m):
        s1 = read_str()
        g[no(s1[0])][no(s1[1])] = False
        g[no(s1[1])][no(s1[0])] = False
    for i in range(n):
        id = no(s[i])
        tmp = 1
        for j in range(MAXNUM):
            if g[id][j]:
                tmp = max(tmp, f[j]+1)
        f[id] = tmp
    print(n-max(f))


if __name__ == '__main__':
    main()