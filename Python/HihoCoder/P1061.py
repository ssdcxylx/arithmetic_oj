# -*- coding:utf-8 -*-


def is_right(temp, counts):
    if ord(temp[0]) + 1 == ord((temp[1])) and ord((temp[1])) + 1 == ord((temp[2])):
        if (counts[0]) >= (counts[1]) and (counts[1]) <= (counts[2]):
            return True
    return False


def main():
    t = input()
    while t > 0:
        n = input()
        str = raw_input()
        temp = [str[0]]
        counts = [1]
        curr = 0
        if len(str) < 3:
            print 'NO'
        else:
            for i in range(1, len(str)):
                if str[i] == temp[curr]:
                    counts[curr] += 1
                else:
                    curr += 1
                    temp.append(str[i])
                    counts.append(1)
                if curr == 3:
                    if is_right(temp, counts):
                        print 'YES'
                        break
                    else:
                        # 压缩空间
                        temp = temp[1:4]
                        counts = counts[1:4]
                        curr = 2
                        if is_right(temp, counts):
                            print 'YES'
                            break
                        elif i == len(str) - 1:
                            print 'NO'
                elif i == len(str) - 1:
                    if curr == 2:
                        if is_right(temp, counts):
                            print 'YES'
                        else:
                            print 'NO'
                    else:
                        print 'NO'
        t -= 1


if __name__ == '__main__':
    main()