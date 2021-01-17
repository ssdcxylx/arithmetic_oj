# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-21 09:01:48
# LastEditTime: 2020-12-21 09:51:11
# LastEditors: ssdcxy
# Description: 使用最小花费爬楼梯
# FilePath: /arithmetic_oj/LeetCode/P0764.py

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = 0
        for i in range(n):
            if i < 2:
                continue
            if i == 2:
                 prev1, prev2 = min(cost[0], cost[1]), 0
            minCost = min(prev1 + cost[i], prev2 + cost[i-1])
            prev1, prev2 = minCost, prev1
        return minCost

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
            cost = stringToIntegerList(line);
            
            ret = Solution().minCostClimbingStairs(cost)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()