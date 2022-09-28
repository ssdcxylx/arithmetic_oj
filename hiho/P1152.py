# -*- coding:utf-8 -*-


def main():
    str = raw_input()
    fab_lst = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    res = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            str1 = str[i:j+1]
            set1 = set(list(str1))
            if len(set1) in fab_lst:
                res.add(str1)
    for x in sorted(res):
        print x


if __name__ == '__main__':
    main()