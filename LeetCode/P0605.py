# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-10 21:03:40
# LastEditTime: 2019-12-10 21:40:12
# LastEditors: ssdcxy
# Description: 种花问题
# FilePath: /arithmetic_oj/LeetCode/P0605.py
import json
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i, m = 0, len(flowerbed)
        while i < m and count < n:
            if flowerbed[i] == 1:
                i += 1
                continue
            pre = 0 if i == 0 else flowerbed[i-1]
            next = 0 if i == m - 1 else flowerbed[i+1]
            if pre == 0 and next == 0:
                count += 1
                flowerbed[i] = 1
            i += 1
        return count >= n


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
            flowerbed = stringToIntegerList(line)
            line = next(lines)
            n = int(line)

            ret = Solution().canPlaceFlowers(flowerbed, n)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
