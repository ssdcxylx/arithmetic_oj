#  -*- coding:utf-8 -*-
lst = []
min = -1


def is_over(str):
    if 'A' in str and 'B' in str and 'C' in str:
        return True
    return False


def main():
    n = input()
    min = 1e5
    for i in range(n):
        lst.append(raw_input().split())
    for i in range(n):
        if is_over((lst[i])[1]):
            cost = int((lst[i])[0])
            if min > cost:
                min = cost
        else:
            for j in range(i+1, n):
                str = (lst[i])[1] + (lst[j])[1]
                if is_over(str):
                    cost = int((lst[i])[0]) + int((lst[j])[0])
                    if min > cost:
                        min = cost
                else:
                    for k in range(j+1, n):
                        str = (lst[i])[1] + (lst[j])[1] + (lst[k])[1]
                        if is_over(str):
                            cost = int((lst[i])[0]) + int((lst[j])[0]) + int((lst[k])[0])
                            if min > cost:
                                min = cost
    if min == 1e5:
        print -1
    else:
        print min


if __name__ == '__main__':
    main()