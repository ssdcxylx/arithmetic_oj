# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-07 12:59:58
# LastEditTime: 2020-03-07 15:07:53
# LastEditors: ssdcxy
# Description: 最多能完成排序的块
# FilePath: /arithmetic_oj/LeetCode/P0769.py

import json
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 0
        ret = 0
        right = arr[0]
        n = len(arr)
        for i in range(n):
            right = max(right, arr[i])
            if right == i: ret += 1
        return ret
            

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
            arr = stringToIntegerList(line);
            
            ret = Solution().maxChunksToSorted(arr)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()