# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-07 14:56:44
# LastEditTime: 2021-01-07 14:57:37
# LastEditors: ssdcxy
# Description: 除法求值
# FilePath: /arithmetic_oj/LeetCode/P0399.py

import json
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dct = dict()
        def find(x):
            if x not in dct:
                dct[x] = (x, 1)
            elif x != dct[x][0]:
                px = find(dct[x][0])
                dct[x] = (px[0], px[1] * dct[x][1])
            return dct[x]
        def union(x, y, multiple):
            px = find(x)
            py = find(y)
            dct[px[0]] = (py[0], multiple*py[1]/px[1])
        for i in range(len(values)):
            x, y, multiple = equations[i][0], equations[i][1], values[i]
            union(x, y, multiple)
        res = []
        for query in queries:
            if query[0] not in dct or query[1] not in dct:
                res.append(-1.0)
            else:
                p0, p1 = find(query[0]), find(query[1])
                if p0[0] != p1[0]:
                    res.append(-1.0)
                else:
                    res.append(p0[1]/p1[1])
        return res

def stringToString2dArray(input):
    return json.loads(input)

def stringToDoubleList(input):
    return json.loads(input)

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
            line = lines.next()
            equations = stringToString2dArray(line)
            line = lines.next()
            values = stringToDoubleList(line)
            line = lines.next()
            queries = stringToString2dArray(line)
            
            ret = Solution().calcEquation(equations, values, queries)

            out = doubleListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()