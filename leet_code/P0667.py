# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 11:26:36
# LastEditTime: 2020-03-07 11:43:23
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0667.py

import json
from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ret = [0] * n
        ret[0] = 1
        tmp = k
        for i in range(1, n):
            ret[i] = ret[i-1] + tmp if i % 2 == 1 else ret[i-1] - tmp
            tmp -= 1
        for i in range(k+1, n):
            ret[i] = i + 1
        return ret

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
            line = next(lines)
            k = int(line);
            
            ret = Solution().constructArray(n, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()