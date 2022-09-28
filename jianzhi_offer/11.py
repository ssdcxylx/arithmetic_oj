# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 08:26:22
# LastEditTime: 2020-11-24 10:37:08
# LastEditors: ssdcxy
# Description: 旋转数组的最小数字
# FilePath: /arithmetic_oj/JianzhiOffer/11.py

import json
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            mid = low + (high - low) // 2 
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high -= 1
        return numbers[low]

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
            numbers = stringToIntegerList(line);
            
            ret = Solution().minArray(numbers)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()