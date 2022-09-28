# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 08:07:18
# LastEditTime: 2020-03-12 08:17:41
# LastEditors: ssdcxy
# Description: 字符串的最大公因子
# FilePath: /arithmetic_oj/LeetCode/P1071.py

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a%b)
        if not ((str1 + str2) == (str2 + str1)):
            return ""
        return str1[0: gcd(len(str1), len(str2))]

        

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
            str1 = stringToString(line);
            line = next(lines)
            str2 = stringToString(line);
            
            ret = Solution().gcdOfStrings(str1, str2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()