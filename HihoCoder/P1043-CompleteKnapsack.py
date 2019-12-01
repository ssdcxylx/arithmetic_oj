# -*- coding: utf-8 -*-


def main():
    (n, m) = (int(x) for x in raw_input().split())
    need = [0 for i in range(0, n)]
    value = [0 for i in range(0, n)]
    for i in range(0, n):
        (need[i], value[i]) = (int(x) for x in raw_input().split())
    best = [0 for i in range(0, m+1)]
    for i in range(0, n):
        for j in range(need[i], m+1):
            best[j] = max(best[j], best[j-need[i]] + value[i])
    print best[m]


if __name__ == '__main__':
    main()