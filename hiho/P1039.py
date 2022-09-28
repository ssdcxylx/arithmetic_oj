# -*- coding:utf-8 -*-


def delete(lst):
    i = 0
    length = len(lst)
    while i < length - 1:
        j = i
        while j < len(lst) - 1 and lst[j] == lst[j+1]:
            j = j + 1
        if (j - i) != 0:
            for k in range(0, j - i + 1):
                lst.pop(i)
        else:
            i = i + 1
    if can_delete(lst):
        return delete(lst)
    else:
        return lst


def can_delete(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i+1]:
            return True
    return False


def main():
    t = int(raw_input())
    while t > 0:
        t = t - 1
        str = raw_input()
        max = 0
        lst = list(str)
        for i in range(0, len(str)+1):
            for j in ['A', 'B', 'C']:
                lst = list(str)
                lst.insert(i, j)
                length1 = len(lst)
                lst = delete(lst)
                length2 = len(lst)
                if length1 - length2 > max:
                    max = length1 - length2
        print max


if __name__ == "__main__":
    main()


