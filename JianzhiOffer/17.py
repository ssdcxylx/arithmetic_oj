# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:19:07
# LastEditTime: 2020-03-10 10:21:02
# LastEditors: ssdcxy
# Description: 打印从1到最大的n位数
# FilePath: /arithmetic_oj/JianzhiOffer/17.py

import json
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        import math
        num = math.pow(10, n)
        return [i for i in range(1, num)]

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            n = int(line);
            
            ret = Solution().printNumbers(n)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()