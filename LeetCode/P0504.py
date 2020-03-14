# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 15:57:17
# LastEditTime: 2020-02-22 16:36:54
# LastEditors: ssdcxy
# Description: 七进制数
# FilePath: /arithmetic_oj/LeetCode/P0504.py

class Solution:
    def convertToBase7(self, num: int) -> str:
        flag, res = "", ""
        if num < 0:
            flag = "-"
            num = -num
        while num / 7 >= 1:
            res += str(num%7)
            num //= 7
        if num != 0:
            res += str(num)
        return flag + res[::-1]
            
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
            
            ret = Solution().convertToBase7(num)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()