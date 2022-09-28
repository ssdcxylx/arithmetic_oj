# -*- coding:utf-8 -*-


def main():
    t = int(raw_input())
    lst = [[] for i in range(t)]
    for i in range(t):
        lst[i] = list(map(int, raw_input().split()))
    best = [
        [0 for i in range(t)]
        for j in range(t)
    ]
    if t > 0:
        best[0][0] = lst[0][0]
    if t > 1:
        best[1][0] = best[0][0] + lst[1][0]
        best[1][1] = best[0][0] + lst[1][1]
    for i in range(2, t):
        for j in range(0, i+1):
            if j == 0:
                best[i][j] = best[i-1][j] + lst[i][j]
            else:
                best[i][j] = max(best[i-1][j], best[i-1][j-1]) + lst[i][j]
    print max(best[t-1])


if __name__ == '__main__':
    main()