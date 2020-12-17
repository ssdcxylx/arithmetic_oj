# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 09:00:57
# LastEditTime: 2020-12-06 22:14:22
# LastEditors: ssdcxy
# Description: 第一个只出现一次的字符
# FilePath: /arithmetic_oj/JianzhiOffer/50.py

import json

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = c not in dic
        for k, v in dic.items():
            if v: return k
        return " "
        

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