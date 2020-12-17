# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 17:53:48
# LastEditTime: 2020-03-20 07:35:58
# LastEditors: ssdcxy
# Description: 格雷编码
# FilePath: /arithmetic_oj/LeetCode/P0089.py

import json
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head << 1
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
            n = int(line);
            
            ret = Solution().grayCode(n)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()