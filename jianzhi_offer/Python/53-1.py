# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 10:25:36
# LastEditTime: 2020-12-08 12:29:27
# LastEditors: ssdcxy
# Description: 在排序数组中查找数字 I
# FilePath: /arithmetic_oj/JianzhiOffer/53-1.py

import json
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        if target not in nums: return 0
        n = len(nums)
        left, right = 0, n - 1
        count = 0 
        while left <= right:
            mid = left + ((right - left)>>1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                start = end = mid
                while start - 1 >= left and nums[start-1] == target:
                    start -= 1
                while end + 1 <= right and nums[end+1] == target:
                    end += 1
                return end - start + 1
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