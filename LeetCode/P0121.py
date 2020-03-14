# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 22:55:57
# LastEditTime: 2020-03-13 08:17:11
# LastEditors: ssdcxy
# Description: 买卖股票的最佳时机
# FilePath: /arithmetic_oj/LeetCode/P0121.py


import json
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = float('inf'), 0
        for x in prices:
            if low > x:
                low = x
            else:
                get = x - low
                if get > profit:
                    profit = get
        return profit


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
