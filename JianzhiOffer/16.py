# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:08:37
# LastEditTime: 2020-03-10 10:18:32
# LastEditors: ssdcxy
# Description: 数值的整数次方
# FilePath: /arithmetic_oj/JianzhiOffer/16.py

class Solution:
    def myPow(self, x: float, n: int) -> float:
        rem = 1
        while n:
            if n % 2: rem = (rem * x)
            x = x ** 2
            n //= 2
        return rem
            

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
            line = lines.next()
            x = stringToDouble(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().myPow(x, n)

            out = doubleToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()