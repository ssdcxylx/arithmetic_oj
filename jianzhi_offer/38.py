# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 15:10:11
# LastEditTime: 2020-12-03 11:46:26
# LastEditors: ssdcxy
# Description: 字符串的排列
# FilePath: /arithmetic_oj/JianzhiOffer/38.py

import json
from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        def backtrack(lst):
            if len(lst) == 1:
                stack.append(lst[0])
                res.append("".join(stack))
                stack.pop()
                return
            for i in range(len(lst)):
                lst[0], lst[i] = lst[i], lst[0]
                stack.append(lst[0])
                backtrack(lst[1:])
                stack.pop()
                lst[0], lst[i] = lst[i], lst[0]
        if not s: return []
        s = list(s)
        stack = []
        res = []
        backtrack(s)
        return list(set(res))

    
    def combination(self, s: str) -> List[str]:
        def backtrack(lst, l):
            if len(lst) < l:
                return
            if l == 0:
                res.append("".join(stack))
                return
            stack.append(lst[0])
            backtrack(lst[1:], l-1)
            stack.pop()
            backtrack(lst[1:], l)
        if not s: return []
        res = []
        stack = []
        s = list(s)
        for i in range(len(s)):
            backtrack(s, i+1)
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