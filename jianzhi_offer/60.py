# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:18:14
# LastEditTime: 2020-12-14 11:15:10
# LastEditors: ssdcxy
# Description: n个骰子的点数
# FilePath: /arithmetic_oj/JianzhiOffer/60.py

from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        pre = [1/6] * 6
        for i in range(2, n+1):
            cur = [0] * (5*i+1)
            for j in range(len(pre)):
                for k in range(6):
                    cur[j+k] += pre[j]/6
            pre = cur
        return cur

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