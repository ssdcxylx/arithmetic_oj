# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 23:05:30
# LastEditTime: 2019-12-10 20:20:25
# LastEditors: ssdcxy
# Description: 买卖股票的最佳时机 II
# FilePath: /arithmetic_oj/LeetCode/P0122.py


import json
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        low, high = float('inf'), 0
        curr = 0
        for x in prices:
            if low > x:
                total += curr
                curr = 0
                low = x
                high = x
            else:
                if high < x:
                    high = x
                else:
                    total += curr
                    curr = 0
                    low = x
                    high = x
            if high - low > curr:
                curr = high - low
        if curr != 0:
            total += curr
        return total


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
            prices = stringToIntegerList(line)

            ret = Solution().maxProfit(prices)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
