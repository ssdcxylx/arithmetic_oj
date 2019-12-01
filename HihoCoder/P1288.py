# -*- coding:utf-8 -*-


def main():
    t = input()
    while t > 0:
        (n, p, w, h) = (int(x) for x in raw_input().split())
        lst = raw_input().split(' ')
        lst = list(map(int, lst))
        font = min(w, h)
        _p = 0
        for i in range(font, 0, -1):
            line = 0
            for x in lst:
                if x % (w // i) == 0:
                    line += x / (w // i)
                else:
                    line += x // (w // i) + 1
            if line % (h // i) == 0:
                _p = line / (h // i)
            else:
                _p = line // (h // i) + 1
            if _p <= p:
                print i
                break
        t -= 1


if __name__ == '__main__':
    main()