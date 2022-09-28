# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 09:42:42
# LastEditTime: 2020-03-03 10:01:10
# LastEditors: ssdcxy
# Description: 每日温度
# FilePath: /arithmetic_oj/LeetCode/P0739.py

from typing import List
import json

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack  = list()
        res = [0 for i in range(n)]
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)
        return res

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            T = stringToIntegerList(line);
            
            ret = Solution().dailyTemperatures(T)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()