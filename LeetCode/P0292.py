# -*- coding: utf-8 -*-
# @time       : 2019-10-24 22:44
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0292.py
# @description: Nim游戏


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
            n = int(line);

            ret = Solution().canWinNim(n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()