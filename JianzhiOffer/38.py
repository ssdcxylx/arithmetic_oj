# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 15:10:11
# LastEditTime: 2020-03-11 15:44:06
# LastEditors: ssdcxy
# Description: 字符串的排列
# FilePath: /arithmetic_oj/JianzhiOffer/38.py

import json
from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        def backtrack(s):
            if len(s) == 1:
                tmp.append(s[0])
                res.append("".join(tmp))
                tmp.pop()
                return 
            for i in range(len(s)):
                if i != 0 and s[i] == s[0]:
                    continue
                s[0], s[i] = s[i], s[0]
                tmp.append(s[0])
                backtrack(s[1:])
                tmp.pop()
                s[i], s[0] = s[0], s[i]
        if not s: return []
        s = list(s)
        res = []
        tmp = []
        backtrack(s)
        return list(set(res))
        
        

def stringToString(input):
    return input[1:-1]

def stringArrayToString(input):
    return json.dumps(input)

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
            
            ret = Solution().permutation(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()