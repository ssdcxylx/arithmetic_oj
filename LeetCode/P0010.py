# -*- coding: utf-8 -*-
# @time       : 2019-10-19 22:43
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0010.py
# @description: 正则表达式匹配


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1, l2 = len(s)+1, len(p)+1
        dp = [[False for _ in range(l2)] for _ in range(l1)]
        dp[0][0] = True
        for i in range(1, l2):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
        for i in range(1, l1):
            for j in range(1, l2):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = (dp[i][j-2] or dp[i-1][j])
                    else:
                        dp[i][j] = dp[i][j-2]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]


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
            s = line;
            line = next(lines)
            p = line;

            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()