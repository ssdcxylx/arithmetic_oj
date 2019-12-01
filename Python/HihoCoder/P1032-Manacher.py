# -*- coding:utf-8 -*-


def manacher(lst):
    length = len(lst)
    p = [0 for i in range(0, length)]
    id = 0
    mx = 0
    max_len = -1
    for i in range(1, length - 1):
        if i < mx:
            p[i] = min(p[2 * id - i], mx - i)
        else:
            p[i] = 1
        while lst[i - p[i]] == lst[i + p[i]]:
            p[i] += 1
        if mx < i + p[i]:
            id = i
            mx = i + p[i]
        max_len = max(max_len, p[i] - 1)
    return max_len


def main():
    t = int(raw_input())
    while t > 0:
        str = raw_input()
        str = '$' + str + '@'
        temp = '#'.join(str)
        print manacher(temp)
        t -= 1


if __name__ == '__main__':
    main()