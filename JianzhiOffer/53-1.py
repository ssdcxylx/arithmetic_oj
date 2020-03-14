# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 10:25:36
# LastEditTime: 2020-03-12 10:34:01
# LastEditors: ssdcxy
# Description: 在排序数组中查找数字 I
# FilePath: /arithmetic_oj/JianzhiOffer/53-1.py

import json
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) >> 1
            if target == nums[mid]:
                count = 1
                left = mid - 1
                right = mid + 1
                while left >= start and nums[left] == target:
                    count += 1
                    left -= 1
                while right <= end and nums[right] == target:
                    count += 1
                    right += 1
                return count 
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return 0



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
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().search(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()