# -*- coding:utf-8 -*-
maxn = 100 + 1
INF = int(1e8)

map = [[INF for x in range(maxn)] for y in range(maxn)]


def floyd(n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (map[i][k] + map[k][j]) <= map[i][j]:
                    map[i][j] = map[i][k] + map[k][j]


def main():
    (n, m) = (int(x) for x in raw_input().split())
    for i in range(n+1):
        map[i][i] = 0
    for i in range(m):
        (u_i, v_i, length_i) = (int(x) for x in raw_input().split())
        if length_i < map[u_i][v_i]:
            map[u_i][v_i] = length_i
            map[v_i][u_i] = length_i
    floyd(n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print map[i][j],
        print


if __name__ == '__main__':
    main()