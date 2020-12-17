# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 15:09:05
# LastEditTime: 2020-04-02 19:11:24
# LastEditors: ssdcxy
# Description: 零钱兑换
# FilePath: /arithmetic_oj/LeetCode/P0322.py

import json
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1


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
            coins = stringToIntegerList(line);
            line = next(lines)
            amount = int(line);
            
            ret = Solution().coinChange(coins, amount)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()