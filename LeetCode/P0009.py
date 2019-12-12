# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-24 22:16:36
# LastEditTime: 2019-12-10 20:15:01
# LastEditors: ssdcxy
# Description: 回文数
# FilePath: /arithmetic_oj/LeetCode/P0009.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        _str = str(x)
        _str_ = _str[::-1]
        if _str_ == _str:
            return True
        return False


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
            x = int(line)

            ret = Solution().isPalindrome(x)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
