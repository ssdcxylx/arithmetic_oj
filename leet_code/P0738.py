# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-15 10:45:40
# LastEditTime: 2020-12-15 11:06:54
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0738.py

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if not N: return 0
        digits = []
        while N:
            digits.append(N%10)
            N //= 10
        n = len(digits)
        pre = 0
        for i in range(1, n):
            if digits[i] < digits[i-1]:
                digits[i-1] -= 1
                pre = i
        for i in range(pre):
            digits[i] = 9
        res = 0
        for i in range(n-1,-1,-1):
            res = res*10 + digits[i]
        return res
        

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
            N = int(line);
            
            ret = Solution().monotoneIncreasingDigits(N)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()