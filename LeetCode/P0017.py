# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 10:22:58
# LastEditTime: 2020-02-20 10:43:58
# LastEditors: ssdcxy
# Description: 电话号码的字母组合
# FilePath: /arithmetic_oj/LeetCode/P0017.py

import json
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def get_chars(digit):
            if digit == 1:
                chars = []
            elif digit == 7:
                pos = (digit-2)*3+96
                chars = [chr(pos+1), chr(pos+2), chr(pos+3), chr(pos+4)]
            elif digit == 8:
                pos = (digit-2)*3+96+1
                chars = [chr(pos+1), chr(pos+2), chr(pos+3)]
            elif digit == 9:
                pos = (digit-2)*3+96+1
                chars = [chr(pos+1), chr(pos+2), chr(pos+3), chr(pos+4)]
            else:
                pos = (digit-2)*3+96
                chars = [chr(pos+1), chr(pos+2), chr(pos+3)]
            return chars
        def backtrack(i, tmp):
            if i == n:
                res.append(tmp)
                return 
            if not _dict[i]:
                backtrack(i+1, tmp)
            else:
                for j in _dict[i]:
                    backtrack(i+1, tmp+j)
        if not digits:
            return []
        _dict = []
        n = len(digits)
        for digit in digits:
            _dict.append(get_chars(int(digit)))
        res = []
        backtrack(0, '')
        return res
        
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
            digits = stringToString(line)
            
            ret = Solution().letterCombinations(digits)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()