# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 23:36:55
# LastEditTime: 2019-12-10 20:24:34
# LastEditors: ssdcxy
# Description: Nim 游戏
# FilePath: /arithmetic_oj/LeetCode/P0292.py


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True


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
            n = int(line)

            ret = Solution().canWinNim(n)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
