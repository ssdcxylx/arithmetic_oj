# -*- coding: utf-8 -*-


def get_next(lst):
    length = len(lst)
    next = [0 for x in range(len(lst)+1)]
    for i in range(1, length):
        j = i
        while j > 0:
            j = next[j]
            if lst[j] == lst[i]:
                next[i + 1] = j + 1
                break
    return next


def kmp(a, b, next):
    num = 0
    j = 0
    length1 = len(a)
    length2 = len(b)
    for i in range(0, length1):
        if j < length2 and a[i] == b[j]:
            j += 1
        else:
            while j > 0:
                j = next[j]
                if a[i] == b[j]:
                    j += 1
                    break
        if j == length2:
            num += 1
    return num


def main():
    t = int(raw_input())
    while t > 0:
        b = list(raw_input())
        a = list(raw_input())
        next = get_next(b)
        print kmp(a, b, next)
        t -= 1


if __name__ == '__main__':
    main()