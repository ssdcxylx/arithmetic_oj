# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-18 10:12:28
# LastEditTime: 2020-12-18 10:19:02
# LastEditors: ssdcxy
# Description: 找不同
# FilePath: /arithmetic_oj/LeetCode/P0389.py

import json

class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        # chars = [0] * 26
        # for c in s:
        #     chars[ord(c)-ord('a')] += 1
        # for c in t:
        #     pos = ord(c)-ord('a')
        #     if chars[pos]:
        #         chars[pos] -= 1
        #     else:
        #         return c
        # return ""

        res = 0
        for c in s:
            res ^= ord(c)
        for c in t:
            res ^= ord(c)
        return chr(res)



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
            line = lines.next()
            s = stringToString(line)
            line = lines.next()
            t = stringToString(line)
            
            ret = Solution().findTheDifference(s, t)

            out = charToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()