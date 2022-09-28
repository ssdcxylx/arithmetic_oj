# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-06 11:04:49
# LastEditTime: 2020-03-06 12:08:54
# LastEditors: ssdcxy
# Description: 最大单词长度乘积
# FilePath: /arithmetic_oj/LeetCode/P0318.py

from typing import List
import json

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        val = [0] * n
        for i in range(n):
            for c in words[i]:
                val[i] |= 1 << (ord(c) - ord('a'))
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if val[i] & val[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret
                

def stringToStringArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            words = stringToStringArray(line)
            
            ret = Solution().maxProduct(words)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()