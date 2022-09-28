# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-10 21:58:02
# LastEditTime: 2019-12-10 23:31:33
# LastEditors: ssdcxy
# Description: 非递减数列
# FilePath: /arithmetic_oj/LeetCode/P0665.py
import json
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 1
        m = len(nums)
        for i in range(1, m):
            if nums[i] < nums[i-1]:
                if count > 0:
                    count -= 1
                    if i - 2 >= 0 and nums[i] < nums[i-2]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i-1] = nums[i]
                else:
                    return False
        return True


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
            nums = stringToIntegerList(line)

            ret = Solution().checkPossibility(nums)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
