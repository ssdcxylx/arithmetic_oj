# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 12:10:14
# LastEditTime: 2020-03-05 14:23:37
# LastEditors: ssdcxy
# Description: 4的幂
# FilePath: /arithmetic_oj/LeetCode/P0342.py

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and (num & 0b0101010101010101010101010101010101010101) != 0
        
        
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
            num = int(line);
            
            ret = Solution().isPowerOfFour(num)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()