# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 07:45:25
# LastEditTime: 2020-02-23 07:53:45
# LastEditors: ssdcxy
# Description: 数组中乘积最大的三个数
# FilePath: /arithmetic_oj/LeetCode/P0628.py

import json
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        _inf = float('inf')
        max1, max2, max3, min1, min2 = -_inf, -_inf, -_inf, _inf, _inf
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)
            

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
            
            ret = Solution().maximumProduct(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()