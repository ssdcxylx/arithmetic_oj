# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:07:39
# LastEditTime: 2020-03-13 08:17:34
# LastEditors: ssdcxy
# Description: 股票的最大利润
# FilePath: /arithmetic_oj/JianzhiOffer/63.py

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur, profit = float('inf'), 0
        for price in prices:
            if price < cur:
                cur = price
            else:
                get = price - cur
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
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()