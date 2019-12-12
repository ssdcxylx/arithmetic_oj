# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-16 10:10:19
# LastEditTime: 2019-12-10 20:13:47
# LastEditors: ssdcxy
# Description: 无重复字符的的最长子串
# FilePath: /arithmetic_oj/LeetCode/P0003.py


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        max_l = 1
        index, l = 0, 1
        for i in range(1, n):
            if s[i] not in s[index:index+l]:
                l += 1
                if l >= max_l:
                    max_l = l
            else:
                index = s[i-l:i].index(s[i]) + (i - l) + 1
                l = i - index + 1
        return max_l


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

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
