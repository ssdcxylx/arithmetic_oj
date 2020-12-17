# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:36:44
# LastEditTime: 2020-12-15 13:38:07
# LastEditors: ssdcxy
# Description: 把字符串转换成整数
# FilePath: /arithmetic_oj/JianzhiOffer/67.py

class Solution:
    def strToInt(self, s: str) -> int:
        if not str: return 0
        res, beign, sign = 0, 0, 1
        int_max, int_min, pre_max = 2**31-1, -2**31, 2**31//10
        length = len(str)
        while str[beign] == ' ':
            beign += 1
            if beign == length: return 0
        if str[beign] in "+-":
            if str[beign] == '-':
                sign = -1
            beign += 1
        for c in str[beign:]:
            if not '0' <= c <= '9': break
            if res > pre_max or (res == pre_max and c > '7'):
                return int_max if sign == 1 else int_min
            res = res * 10 + ord(c) - ord('0')
        return sign * res
 

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
            a = stringToString(line);
            
            ret = Solution().strToInt(a)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()