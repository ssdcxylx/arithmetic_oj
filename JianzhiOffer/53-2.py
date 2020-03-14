# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 10:36:33
# LastEditTime: 2020-03-12 10:50:40
# LastEditors: ssdcxy
# Description: 0～n-1中缺失的数字
# FilePath: /arithmetic_oj/JianzhiOffer/53-2.py

import json
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start, end = 0, n
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] == mid:
                start = mid + 1
            else:
                end = mid
        return start
            
            

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
            
            ret = Solution().missingNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()