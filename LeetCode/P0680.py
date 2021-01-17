# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 22:35:55
# LastEditTime: 2020-12-22 10:37:01
# LastEditors: ssdcxy
# Description: 验证回文字符串 Ⅱ
# FilePath: /arithmetic_oj/LeetCode/P0680.py

"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
class Solution:
    def valid(self, s: str, low: int, high: int, flag: bool) -> bool:
        def valid(left, right, flag):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return (valid(left+1, right, False) or valid(left, right-1, False)) if flag else False
            return True
        if not s: return True
        if len(s) == 1: return True
        return valid(0, len(s)-1, True)  


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
