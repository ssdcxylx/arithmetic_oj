# -*- coding:utf-8 -*-


def main():
    t = input()
    dict = []
    while t > 0:
        pos1, pos2 = -1, -1
        p = list(raw_input().split())
        op, name1, name2 = int(p[0]), p[1], p[2]
        for i in range(len(dict)):
            if name1 in dict[i]:
                pos1 = i
            if name2 in dict[i]:
                pos2 = i
        if op == 0:
            if pos1 == -1 and pos2 == -1:
                dict.append([name1, name2])
            elif pos1 == -1 and pos2 != -1:
                dict[pos2].append(name1)
            elif pos1 != -1 and pos1 == -1:
                dict[pos1].append(name2)
            elif pos1 != pos2:
                dict.append(dict[pos1] + dict[pos2])
                dict.remove(dict[pos1])
                dict.remove(dict[pos2])
        else:
            if pos1 == -1 or pos2 == -1:
                print 'no'
            elif pos1 != pos2:
                print 'no'
            else:
                print 'yes'
        t -= 1


if __name__ == '__main__':
    main()