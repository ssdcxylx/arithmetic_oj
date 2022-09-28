# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 08:32:57
# LastEditTime: 2020-02-21 08:56:25
# LastEditors: ssdcxy
# Description: 解码方法
# FilePath: /arithmetic_oj/LeetCode/P0091.py
import json

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s or s[0] == "0":
            return 0
        a, b = 1, 1
        for i in range(1, n):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    b = a
                else:
                    return 0
            else:
                if s[i-1] == "1" or (s[i-1] == "2" and "1" <= s[i] <= "6"):
                    a, b = b, a + b
                else:
                    a = b
        return b
                
        

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
            s = stringToString(line);
            
            ret = Solution().numDecodings(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()