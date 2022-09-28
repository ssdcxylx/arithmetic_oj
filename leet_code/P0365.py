# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 08:30:38
# LastEditTime: 2020-03-21 08:50:20
# LastEditors: ssdcxy
# Description: 水壶问题
# FilePath: /arithmetic_oj/LeetCode/P0365.py

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        if x + y < z:
            return False
        if not x or not y:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
            

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
            x = int(line);
            line = next(lines)
            y = int(line);
            line = next(lines)
            z = int(line);
            
            ret = Solution().canMeasureWater(x, y, z)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()