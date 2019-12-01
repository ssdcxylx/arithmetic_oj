# -*- coding: utf-8 -*-
# @time       : 2019-10-24 22:14
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0557.py
# @description: 反转字符串中的单词3


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        tmp = []
        for c in s:
            tmp.append(c[::-1])
        s = ' '.join(tmp)
        return s


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = line

            ret = Solution().reverseWords(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()