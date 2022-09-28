# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 19:36:02
# LastEditTime: 2020-02-22 20:07:59
# LastEditors: ssdcxy
# Description: 二进制加法
# FilePath: /arithmetic_oj/LeetCode/P0067.py


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        res = ""
        carry = 0
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 0:
                res += "0"
            else:
                res += "1"
            carry //= 2
        if carry == 1:
            res += "1"
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
            a = stringToString(line);
            line = next(lines)
            b = stringToString(line);
            
            ret = Solution().addBinary(a, b)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()