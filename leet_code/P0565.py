# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 12:29:23
# LastEditTime: 2020-03-07 12:58:51
# LastEditors: ssdcxy
# Description: 数组嵌套
# FilePath: /arithmetic_oj/LeetCode/P0565.py

import json 
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def reursive(i, val):
            if nums[i] == val: return 1
            if ret[i] != 0: return ret[i]
            if nums[i] != val:
                ret[i] = reursive(nums[i], val) 
            return ret[i] + 1
        n = len(nums)
        ret = [0] * n
        for i in range(n):
            if ret[i] == 0:
                ret[i] = reursive(nums[i], nums[i])
        return max(ret)
                
            

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
            
            ret = Solution().arrayNesting(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()