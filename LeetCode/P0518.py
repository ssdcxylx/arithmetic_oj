# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-21 16:00:24
# LastEditTime: 2020-04-02 19:14:30
# LastEditors: ssdcxy
# Description: 零钱兑换 II
# FilePath: /arithmetic_oj/LeetCode/P0518.py

import json
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]
            
        
        

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
            amount = int(line);
            line = next(lines)
            coins = stringToIntegerList(line);
            
            ret = Solution().change(amount, coins)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()