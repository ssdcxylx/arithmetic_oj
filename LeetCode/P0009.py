# -*- coding: utf-8 -*-
# @time       : 2019-10-19 22:34
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0009.py
# @description: 回文数


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
            x = int(line);

            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
