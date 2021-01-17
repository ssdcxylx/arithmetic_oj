# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-10 21:03:40
# LastEditTime: 2021-01-01 09:27:05
# LastEditors: ssdcxy
# Description: 种花问题
# FilePath: /arithmetic_oj/LeetCode/P0605.py
import json
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        if not flowerbed: return False
        length = len(flowerbed)
        count = 0
        cur = 0
        while cur < length:
            if flowerbed[cur]:
                cur += 1
                continue
            if cur > 0 and flowerbed[cur-1]:
                cur += 1
                continue
            next = 0 if cur == length-1 else flowerbed[cur+1]
            if not next:
                count += 1
                flowerbed[cur] = 1
            cur += 2
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
