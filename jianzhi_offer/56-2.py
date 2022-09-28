# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 11:54:19
# LastEditTime: 2020-03-12 12:07:23
# LastEditors: ssdcxy
# Description: 数组中数字出现的次数 II
# FilePath: /arithmetic_oj/JianzhiOffer/56-2.py

import json
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3:
                res |= bit
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
            


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
            
            ret = Solution().singleNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()