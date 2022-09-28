# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-14 23:24:15
# LastEditTime: 2019-12-15 00:11:24
# LastEditors: ssdcxy
# Description: 划分字符区间
# FilePath: /arithmetic_oj/LeetCode/P0763.py

import json
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        _S = S[::-1]
        n = len(S)
        start, end = 0, 0
        _res = []
        curr = S[0]
        if n == 1:
            return [1]
        for i in range(0, n):
            index = n - _S.index(S[i]) - 1
            if index != i:
                if index > end:
                    curr = S[i]
                    end = index
            if i == end:
                if i != n-1:
                    _res.append(end-start+1)
                    start = end + 1
                    end = start
                    curr = S[start]
        _res.append(end-start+1)
        return _res


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
            S = stringToString(line)

            ret = Solution().partitionLabels(S)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
