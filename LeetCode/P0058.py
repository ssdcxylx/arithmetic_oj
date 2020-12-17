# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-22 10:35:58
# LastEditTime: 2020-03-22 10:57:51
# LastEditors: ssdcxy
# Description: 合并区间
# FilePath: /arithmetic_oj/LeetCode/P0058.py

import json
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

                 



def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            intervals = stringToInt2dArray(line)
            
            ret = Solution().merge(intervals)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()