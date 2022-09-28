# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 20:07:43
# LastEditTime: 2020-02-22 20:15:22
# LastEditors: ssdcxy
# Description: 字符串相加
# FilePath: /arithmetic_oj/LeetCode/P0415.py


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1, num2 = num1.zfill(n), num2.zfill(n)

        res = ""
        carry = 0
        for i in range(n-1, -1, -1):
            _sum = int(num1[i]) + int(num2[i]) + carry
            if _sum >= 10:
                carry = 1
                res += str(_sum - 10)
            else:
                carry = 0
                res += str(_sum)
        if carry == 1:
            res += str(1)
        return res[::-1]
            

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
            num1 = stringToString(line);
            line = next(lines)
            num2 = stringToString(line);
            
            ret = Solution().addStrings(num1, num2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()