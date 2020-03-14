# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 21:59:56
# LastEditTime: 2020-02-20 22:36:33
# LastEditors: ssdcxy
# Description: 等差数列划分
# FilePath: /arithmetic_oj/LeetCode/P0413.py

import json
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3: return 0
        start, mid = A[0], A[1]
        length = 2
        ans = 0
        for i in range(2, n):
            if start + A[i] == 2 * mid:
                ans += length - 1
                length += 1
            else:
                length = 2
            start, mid = mid, A[i]
        return ans

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
            A = stringToIntegerList(line);
            
            ret = Solution().numberOfArithmeticSlices(A)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()