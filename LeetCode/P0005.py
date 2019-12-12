# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-16 09:25:09
# LastEditTime: 2019-12-10 20:55:00
# LastEditors: ssdcxy
# Description: 最长回文子串
# FilePath: /arithmetic_oj/LeetCode/P0005.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        start, max_len = 0, 1
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i > 0 and s[i] == s[i-1]:
                dp[i-1][i] = 1
                start = i - 1
                max_len = 2
        for i in range(2, n):
            k = i
            for j in range(0, n - i):
                if s[k] == s[j]:
                    dp[j][k] = dp[j+1][k-1]
                    if dp[j][k] == 1:
                        start = j
                        max_len = k - j + 1
                k += 1
        return s[start:start+max_len]


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

            ret = Solution().longestPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
