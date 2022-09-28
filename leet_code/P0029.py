# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-16 08:33:19
# LastEditTime: 2020-03-16 09:16:03
# LastEditors: ssdcxy
# Description: 两数相除
# FilePath: /arithmetic_oj/LeetCode/P0029.py

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        ans = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        while count:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                ans += 1 << count
                dividend -= divisor
        if flag: ans = -ans
        return ans if -(1<<31) <= ans < (1<<31) else (1<<31) - 1

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
            dividend = int(line);
            line = next(lines)
            divisor = int(line);
            
            ret = Solution().divide(dividend, divisor)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()