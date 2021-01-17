# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-01 12:42:04
# LastEditTime: 2021-01-01 13:29:48
# LastEditors: ssdcxy
# Description: 分发糖果
# FilePath: /arithmetic_oj/LeetCode/P0135.py

import json
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        inc = dec = pre = ans = 0
        for i in range(n):
            if i == 0:
                inc += 1
                ans += 1
                pre = 1
                continue
            if ratings[i] >= ratings[i-1]:
                dec = 0
                pre = 1 if ratings[i] == ratings[i-1] else pre + 1
                ans += pre
                inc = pre
            else:
                dec += 1
                if inc == dec:
                    dec += 1
                ans += dec
                pre = 1
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
            ratings = stringToIntegerList(line);
            
            ret = Solution().candy(ratings)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()