# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 07:51:01
# LastEditTime: 2020-03-19 08:11:01
# LastEditors: ssdcxy
# Description: 最长公共前缀
# FilePath: /arithmetic_oj/LeetCode/P0014.py

import json
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        n = len(strs)
        ans = strs[0]
        for i in range(1, n):
            j = 0
            cur = min(len(ans), len(strs[i]))
            while j < cur:
                if strs[i][j] != ans[j]:
                    break
                j += 1
            ans = ans[0:j]
            if not ans:
                return ""
        return ans
        
        

def stringToStringArray(input):
    return json.loads(input)

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
            
            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()