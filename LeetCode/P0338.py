# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-06 12:09:46
# LastEditTime: 2020-03-06 12:16:32
# LastEditors: ssdcxy
# Description: 比特位计数
# FilePath: /arithmetic_oj/LeetCode/P0338.py
from typing import List
import json

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num+1):
            res[i] = res[i&(i-1)] + 1
        return res

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
            num = int(line);
            
            ret = Solution().countBits(num)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()