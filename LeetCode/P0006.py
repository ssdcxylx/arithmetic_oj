# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:15:52
# LastEditTime: 2019-12-10 20:14:20
# LastEditors: ssdcxy
# Description: Z字形变换
# FilePath: /arithmetic_oj/LeetCode/P0006.py


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows < 2:
            return s
        zs = [['' for j in range(l)] for i in range(numRows)]
        flag = True
        index, i, j, = 0, 0, 0
        while index < l:
            zs[i][j] = s[index]
            index += 1
            if flag:
                if i == numRows-1:
                    flag = False
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    flag = True
                    i += 1
                else:
                    i -= 1
                    j += 1
        z = ""
        for _zs in zs:
            z += "".join(_zs)
        return z


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
            line = next(lines)
            numRows = int(line)

            ret = Solution().convert(s, numRows)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
