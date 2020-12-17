# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 15:26:40
# LastEditTime: 2020-03-19 15:47:22
# LastEditors: ssdcxy
# Description: 字符串相乘
# FilePath: /arithmetic_oj/LeetCode/P0043.py

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n, m = len(num1), len(num2)
        tmp = [0] * (m+n)
        for i in range(n-1, -1, -1):
            a = ord(num1[i]) - ord('0')
            for j in range(m-1, -1, -1):
                b = ord(num2[j]) - ord('0')
                _sum = tmp[i+j+1] + a * b
                tmp[i+j+1] = _sum % 10
                tmp[i+j] += _sum // 10
        res = []
        for i in range(m+n):
            if i == 0 and tmp[i] == 0: continue
            res.append(str(tmp[i]))
        return "".join(res)

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
            
            ret = Solution().multiply(num1, num2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()