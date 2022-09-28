# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-14 09:46:59
# LastEditTime: 2021-01-14 09:48:11
# LastEditors: ssdcxy
# Description: 可被 5 整除的二进制前缀
# FilePath: /arithmetic_oj/LeetCode/P1018.py

import json
from typing import List

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cur = 0
        res = []
        for num in A:
            cur = (cur * 2 + num) % 5
            res.append(cur == 0)
        return res

def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line);
            
            ret = Solution().prefixesDivBy5(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()