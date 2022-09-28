# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-23 08:19:06
# LastEditTime: 2020-03-23 08:35:20
# LastEditors: ssdcxy
# Description: Pow(x, n)
# FilePath: /arithmetic_oj/LeetCode/P0050.py

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        tmp = n
        if tmp < 0:
            x = 1/x
            tmp = -tmp
        ans = 1
        cur = x
        while tmp:
            if i % 2 == 1:
                ans = ans * cur
            cur = cur * cur
            tmp //= 2
        return ans
        

def stringToDouble(input):
    return float(input)

def stringToInt(input):
    return int(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = stringToDouble(line)
            line = next(lines)
            n = stringToInt(line)
            
            ret = Solution().myPow(x, n)

            out = doubleToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()