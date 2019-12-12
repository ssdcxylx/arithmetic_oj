# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 22:35:55
# LastEditTime: 2019-12-10 20:31:01
# LastEditors: ssdcxy
# Description: 验证回文字符串 Ⅱ
# FilePath: /arithmetic_oj/LeetCode/P0680.py


class Solution:
    def valid(self, s: str, low: int, high: int, flag: bool) -> bool:
        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                if flag:
                    return self.valid(s, low+1, high, False) or self.valid(s, low, high-1, False)
                else:
                    return False
        return True

    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        return self.valid(s, low, high, True)


def stringToString(input):
    return input[1:-1]


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
            s = stringToString(line)

            ret = Solution().validPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
