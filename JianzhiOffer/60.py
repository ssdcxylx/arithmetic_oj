# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:18:14
# LastEditTime: 2020-03-12 14:56:25
# LastEditors: ssdcxy
# Description: n个骰子的点数
# FilePath: /arithmetic_oj/JianzhiOffer/60.py

from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0]*(6*n+1) for _ in range(n+1)]
        for i in range(1, 7): dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for k in range(1, 7):
                    if j - k < i - 1: break
                    dp[i][j] += dp[i-1][j-k]
        total = 6 ** n
        res = [0] * (5*n+1)
        for i in range(n, 6*n+1):
            res[n] = dp[n][i] / total
        return res

def stringToInt(input):
    return int(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def doubleListToString(nums, len_of_list=None):
    if nums is None or len_of_list == 0:
        return "[]"

    if len_of_list is None:
        len_of_list = len(nums)

    serializedDoubles = []
    for num in nums:
        serializedDoubles.append(doubleToString(num))
    return "[{}]".format(','.join(serializedDoubles))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = stringToInt(line)
            
            ret = Solution().twoSum(n)

            out = doubleListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()