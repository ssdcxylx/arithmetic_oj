# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-19 23:03:25
# LastEditTime: 2019-12-20 22:56:19
# LastEditors: ssdcxy
# Description:为运算表达式设计优先级
# FilePath: /arithmetic_oj/LeetCode/P0241.py

from typing import List
import json


class Solution:
    def diffWaysToCompute(self, _input: str) -> List[int]:
        ways = []
        for i, c in enumerate(_input):
            if c in "+-*":
                left = self.diffWaysToCompute(_input[:i])
                right = self.diffWaysToCompute(_input[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            ways.append(l + r)
                        elif c == '-':
                            ways.append(l - r)
                        else:
                            ways.append(l * r)
        if len(ways) == 0:
            ways.append(int(_input))
        return ways


def stringToString(input):
    return input[1:-1]


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
            input = stringToString(line)

            ret = Solution().diffWaysToCompute(input)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
