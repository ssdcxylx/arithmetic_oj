# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 09:00:57
# LastEditTime: 2020-03-12 09:17:08
# LastEditors: ssdcxy
# Description: 第一个只出现一次的字符
# FilePath: /arithmetic_oj/JianzhiOffer/50.py

import json

class Solution:
    def firstUniqChar(self, s: str) -> str:
        lst = []
        for c in s:
            if c not in lst:
                lst.append(c)
            else:
                lst.remove(c)
        if lst: return lst[0]
        else: return " "
        

def stringToString(input):
    return input[1:-1]

def charToString(c):
    return json.dumps(c)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)
            
            ret = Solution().firstUniqChar(s)

            out = charToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()