# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 16:08:57
# LastEditTime: 2020-02-22 16:52:05
# LastEditors: ssdcxy
# Description: 数字转换为十六进制数
# FilePath: /arithmetic_oj/LeetCode/P0405.py

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        if num < 0:
            num = 2 ** 32 + num
        res = ""
        lst = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        while num / 16 >= 1:
            cur = num % 16
            res += lst[cur]
            num //= 16
        if num != 0:
            res += lst[num]
        return res[::-1]
            

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
            
            ret = Solution().toHex(num)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()