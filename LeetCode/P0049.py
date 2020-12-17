# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-25 08:06:52
# LastEditTime: 2020-12-14 10:33:03
# LastEditors: ssdcxy
# Description: 字母异位词分组
# FilePath: /arithmetic_oj/LeetCode/P0049.py

import json
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = {}
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c) - ord('a')] += 1
            mp.setdefault(str(count), []).append(st)
        return list(mp.values())

def stringToStringArray(input):
    return json.loads(input)

def string2dArrayToString(input):
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
            strs = stringToStringArray(line)
            
            ret = Solution().groupAnagrams(strs)

            out = string2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()